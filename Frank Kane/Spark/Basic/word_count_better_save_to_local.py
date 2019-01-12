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

# save word count to a file
file_path = os.getcwd() + "/book_words.txt"
file_handler = open(file_path, "w")

# sorted the result
sorted_result = sorted(retults, key=getKey, reverse=True)
for token in sorted_result:
    file_handler.write((token[0] + " " + str(token[1]) + "\n").decode("utf-8"))
file_handler.close()