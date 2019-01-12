from pyspark import SparkConf, SparkContext
import os

# set the spark context
# Master must either be yarn or start with spark, mesos, k8s, or local
# and it is case senstive
conf = SparkConf().setMaster("local").setAppName("Count Ratings")
sc = SparkContext(conf=conf)

# read the ratings.csv data to start
path_csv = os.getcwd() + "/ratings.csv"
rdd_ratings = sc.textFile(path_csv)

# get all the ratings
rdd_just_ratings = rdd_ratings.map(lambda x: x.split(",")[2])
rdd_countByValue = rdd_just_ratings.countByValue()
print(sorted(rdd_countByValue.items()))

# stop sc to avoid crash and exception
sc.stop()
