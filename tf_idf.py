#! /usr/bin/python
 
import sys
import re
from os import environ
from math import log
from collections import Counter
from stemming.porter2 import stem
from mrjob.job import MRJob
from mrjob.step import MRStep

wc_regex = re.compile(r"\w+")
docs_count = len(sys.argv) - 1

class TF_IDF(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_cw, reducer=self.reducer_cw),
            MRStep(reducer=self.reducer_ctf)
        ]
    def mapper_cw(self, _, line):
        words = wc_regex.finditer(line)
        doc = environ['mapreduce_map_input_file']
        lowered_words = map(lambda w: w.group().lower(), words)
        prepared_words = map(stem, lowered_words)
        words_doc = Counter(prepared_words)
        for word, count in words_doc.items():
            yield ((doc, word), count)

    def reducer_cw(self, d_w, count):
        doc, word = d_w
        yield (word, (doc, sum(count)))

    def reducer_ctf(self, word, stat):
        word_stat = [x for x in stat]
        docs_with_word = len(word_stat)
        total_enc = sum(c for k, c in word_stat)

        for doc, w_in_d_count in word_stat:
            tf_idf = w_in_d_count/total_enc * log(docs_count/docs_with_word)
            yield ((word, doc), tf_idf)

if __name__ == '__main__':
    TF_IDF.run()