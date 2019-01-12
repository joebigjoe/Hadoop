from pyspark import SparkConf, SparkContext
import os
from io import open
import re

# a function using regex to strip just words
def getWords(str_to_match):
    pattern = re.compile(r"\W+")
    str_list = pattern.split(str_to_match.lower())
    return str_list

# set the spark context
# Master must either be yarn or start with spark, mesos, k8s, or local
# and it is case senstive
conf = SparkConf().setMaster("local").setAppName("Word Count Better")
sc = SparkContext(conf=conf)

# this is the start of the code
pathtxt = os.getcwd() + "/book.txt"
rdd_quotes = sc.textFile(pathtxt)

# map will get the word list
#rdd_quotes_word_list = rdd_quotes.map(getWords)
#for token in rdd_quotes_word_list.collect():
    #print(token)

# flatmap
rdd_quotes_words = rdd_quotes.flatMap(getWords)
rdd_quotes_words_pair = rdd_quotes_words.map(lambda x: (x,1)).reduceByKey(lambda x, y: x+y)
reversed_key_value = rdd_quotes_words_pair.map(lambda (x, y):(y,x))
sorted_result = reversed_key_value.sortByKey(ascending=False).collect()

file_path = os.getcwd() + "/book_words_reverse.txt"
file_handler = open(file_path, "w")

for token in sorted_result:
    file_handler.write((str(token[0]) + " " + token[1] + "\n").decode("utf-8"))
file_handler.close()