import os
from pyspark import SparkConf, SparkContext

# local sc
conf = SparkConf().setMaster("local").setAppName("basic operation")
sc = SparkContext(conf=conf)

# data
numbers = [1, 2, 3, 4, 5]
rdd_numbers = sc.parallelize(numbers)

# map
rdd_mpped = rdd_numbers.map(lambda x: (x, 1))
print(rdd_mpped.collect())

# Reduce
rdd_reduced = rdd_mpped.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]))
print(rdd_reduced)

# aggregate 
# the initial number is (0,0)
# in the first step x[0] = 0, x[1] = 0
# then go in the aggregation.
# x,y: still loops the whole RDD, just the first one is the initial value
seqOp = (lambda x, y: (x[0] + y, x[1] + 1))
combOp = (lambda x, y: (x[0] + y[0], x[1] + y[1]))
rdd_aggregated = rdd_numbers.aggregate((0,0), seqOp, combOp)
print(rdd_aggregated)

# foreach
def f(x):
    print(x)

rdd_numbers.foreach(f)

