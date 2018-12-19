import os
from pyspark import SparkConf, SparkContext

# local sc
conf = SparkConf().setMaster("local").setAppName("basic operation")
sc = SparkContext(conf=conf)

# rdd
list_number = [1, 2, 3, 4, 5]
rdd_number = sc.parallelize(list_number)
rdd_number.persist()
rdd_mapped = rdd_number.map(lambda x: x*x*x)
print(rdd_mapped.count())
print(rdd_mapped.first())
print(rdd_mapped.take(2))
