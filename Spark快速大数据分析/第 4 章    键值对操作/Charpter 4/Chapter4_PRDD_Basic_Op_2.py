from pyspark import SparkConf, SparkContext
import os

# get a local sc
conf = SparkConf().setMaster("local").setAppName("paired RDD with movies")
sc = SparkContext(conf=conf)

# make a simple paired RDD
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
rdd_numbers = sc.parallelize(list_numbers)
paird_rdd_numbers = rdd_numbers.map(lambda x: (x, x*x*x))
print(paird_rdd_numbers.collect())

# map values
# for each key, do the same oeration for the values
paird_rdd_numbers_mapValues = paird_rdd_numbers.mapValues(lambda x: x*2)
print(paird_rdd_numbers_mapValues.collect())

# reduce by keys
# when has the same key, combine the value.
# x, y are the values
paird_rdd_numbers_reduceBykeys = paird_rdd_numbers.reduceByKey(
    lambda x, y: x + y)
print(paird_rdd_numbers_reduceBykeys.collect())

# compute average value using mapvalues and reducebykey
rdd_a = paird_rdd_numbers.mapValues(lambda x: (x, 1))
print("rdd_a")
print(rdd_a.collect())

# at this moment, the value is a tuple
# but the whole operation is still manage vlaues, when it is a tuple, we use the tuple method.
# this is to calculate average for each key
# NOT for all the values
rdd_b = rdd_a.reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1]))
print("rdd_b")
print(rdd_b.collect())

# map value is to do the smae op for each key
# so this is will not work
# it is a misuse for reduce and map
# i am using a map, but i am try to combine.
# so we need a nother method
# the following code is WRONG
# this kind of logic is WRONG
#rdd_c = rdd_a.mapValues(lambda x, y: (x[0]+y[0], x[1]+y[1]))
# print("rdd_c")
# print(rdd_c.collect())

# combine the value togather
rdd_c = paird_rdd_numbers.combineByKey((lambda x: (x, 1)), (lambda x, y: (
    x[0]+y, x[1]+1)), (lambda x, y: (x[0]+y[0], x[1]+y[1])))
print("rdd_c")
print(rdd_c.collect())

# then we use another map
# in this map, the operation happens on a tuple
# so the opertion is tuple operation
# (1, (2, 2))
rdd_d = rdd_c.map(lambda x: (x[0], x[1][0]/x[1][1]))
print("rdd_d")
print(rdd_d.collect())
print(rdd_d.collectAsMap())

# another way
# make sure the format you pass to the lambda is the same as (1, (2, 2))
rdd_e = rdd_c.map(lambda (xx, (yy, zz)): (xx, yy/zz))
print("rdd_e")
print(rdd_e.collect())

# stop the sc
sc.stop()
