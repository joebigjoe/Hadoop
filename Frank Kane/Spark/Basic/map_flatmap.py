from pyspark import SparkConf, SparkContext
import os

# set the spark context
# Master must either be yarn or start with spark, mesos, k8s, or local
# and it is case senstive
conf = SparkConf().setMaster("local").setAppName("Lowest Temp")
sc = SparkContext(conf=conf)

# this is the start of the code
pathtxt = os.getcwd() + "/quotes.txt"
rdd_quotes = sc.textFile(pathtxt)
rdd_quotes_mapped = rdd_quotes.map(lambda x: x.split(" "))
print("Mapped:")
print(rdd_quotes_mapped.collect())
rdd_quotes_flatmapped = rdd_quotes.flatMap(lambda x: x.split(" "))

print("FlatMapped:")
print(rdd_quotes_flatmapped.collect())

sc.stop()