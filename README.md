# Вторая лабораторная по большим данным

## TF-IDF

# Использование:

./tf-idf.py -r hadoop <входные данные> <файл, по которму будет осуществляться поиск>

./search.py <файл, по которму будет осуществляться поиск> <слово для поиска>

Например:

./tf-idf.py -r hadoop hdfs://my_home/wiki* > engine

./search.py engine music
