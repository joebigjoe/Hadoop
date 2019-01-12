from pyspark import SparkConf, SparkContext
import os
from io import open

# set the spark context
# Master must either be yarn or start with spark, mesos, k8s, or local
# and it is case senstive
conf = SparkConf().setMaster("local").setAppName("Word Count")
sc = SparkContext(conf=conf)

# this is the start of the code
pathtxt = os.getcwd() + "/book.txt"
rdd_quotes = sc.textFile(pathtxt)

rdd_words = rdd_quotes.flatMap(lambda x: x.lower().split(" "))
rdd_words_tuple = rdd_words.map(lambda x: (x, 1))
rdd_words_counter = rdd_words_tuple.reduceByKey(lambda x, y: x+y)
result = rdd_words_counter.collect()

# sort the result
def getKey(item):
    return item[1]

sorted_result = sorted(result, key=getKey, reverse=False)

for token in sorted_result:
    print(token)