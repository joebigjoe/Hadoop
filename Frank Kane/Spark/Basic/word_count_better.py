from pyspark import SparkConf, SparkContext
import os
from io import open
import re

# a function using regex to strip just words
def getWords(str_to_match):
    pattern = re.compile(r"\W+")
    str_list = pattern.split(str_to_match.lower())
    return str_list

# sort the result
def getKey(item):
    return item[1]

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
retults = rdd_quotes_words.countByValue().items()

sorted_result = sorted(retults, key=getKey)
for token in sorted_result:
    print(token)