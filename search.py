#!/usr/bin/python

import sys
import re
import operator
from stemming.porter2 import stem


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("usage: ./search <where (tf_idf output)> <what>")
  
  s_word = sys.argv[2]
  result = {}

  wc_regex = re.compile(r"[\w/._-]+")
  with open(sys.argv[1], 'r') as tf_tfinv_file:
    for line in tf_tfinv_file:
      values = wc_regex.findall(line)
#      word, doc, val = (*values, )
      word, doc, val = ("".join(values[:-2]), values[-2], values[-1])
      if word == s_word:
        result[doc] = (doc, val)

  for x in sorted(result, key=operator.itemgetter(1), reverse=True):
    doc, val = result[x]
    print("{0} (value = {1})".format(*result[x]))