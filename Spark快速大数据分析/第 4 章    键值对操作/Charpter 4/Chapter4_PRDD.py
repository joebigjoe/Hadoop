from pyspark import SparkConf, SparkContext
import os

# get a local sc
conf = SparkConf().setMaster("local").setAppName("paired RDD with movies")
sc = SparkContext(conf=conf)

# load the local data
localFilePath = os.getcwd() + "/movies10.csv"
rdd_movies10 = sc.textFile(localFilePath)
print(type(rdd_movies10))
print(rdd_movies10.collect())

# changed to pair RDD
pair_rdd_movies10 = rdd_movies10.map(lambda x: (x.split(",")[0], x))
print(type(pair_rdd_movies10))
print(pair_rdd_movies10.collect())

sc.stop()