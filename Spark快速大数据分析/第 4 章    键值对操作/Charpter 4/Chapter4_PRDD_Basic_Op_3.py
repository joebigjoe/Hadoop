from pyspark import SparkConf, SparkContext
import os

# get a local sc
conf = SparkConf().setMaster("local").setAppName("paired RDD with movies")
sc = SparkContext(conf=conf)

# load the local data
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
pair_rdd = sc.parallelize(list_number).map(lambda x: (x, x*x*x))
print(pair_rdd.collect())

# grop by key
pair_rdd_groupbykey = pair_rdd.groupByKey()
print(pair_rdd_groupbykey.collect())

# cogroup
list_name = [(1, "joey"), (1, "aria"), (2, "massie"), (2, "he"),
          (3, "bear"), (4, "bi"), (5, "nan"), (6, "wei")]
pair_rdd_names = sc.parallelize(list_name)
pair_rdd_cogroup = pair_rdd.cogroup(pair_rdd_names)
print(pair_rdd_cogroup.collect())

# i will do some deep learning for interator from the python training
