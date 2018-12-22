from pyspark import SparkConf, SparkContext
import os

# get a local sc
conf = SparkConf().setMaster("local").setAppName("paired RDD with movies")
sc = SparkContext(conf=conf)

# load the local data
list_number = [1,2,3,4,5,6,7,8,9,0]
pair_rdd = sc.parallelize(list_number).map(lambda x:(x, x*x*x))
print(pair_rdd.collect())

# filter
pair_rdd_filtered = pair_rdd.filter(lambda (x,y): x > 5)
print(pair_rdd_filtered.collect())

# the vesion of word count which i understand now
wordFilePath =  os.getcwd() + "/BoxOfficeMojo.txt"
rdd_lines = sc.textFile(wordFilePath)
rdd_words = rdd_lines.flatMap(lambda x: x.split(" "))
rdd_words_keypair = rdd_words.map(lambda x: (x, 1))
print(rdd_words_keypair.collect())

rdd_key_combined = rdd_words_keypair.reduceByKey(lambda x,y: x+y)
print(rdd_key_combined.collect())

# never forget the stop
sc.stop()