from pyspark import SparkConf, SparkContext

# initialize local sc
conf = SparkConf().setMaster("local").setAppName("Spark Basic Opreation")
sc = SparkContext(conf=conf)

# test set 1
dialogs1 = ["Apple Apple apple cabage banana pear tomato"]
rdd_dialogs1 = sc.parallelize(dialogs1)
rdd_words1 = rdd_dialogs1.flatMap(lambda x: x.split(" "))
print(rdd_words1.collect())

# test set 2
dialogs2 = ["onion cucumber cabage beans tomato"]
rdd_dialogs2 = sc.parallelize(dialogs2)
rdd_words2 = rdd_dialogs2.flatMap(lambda x: x.split(" "))
print(rdd_words2.collect())

# distinct
print("distinct rdd1 " + str(rdd_words1.distinct().collect()))

# union
rdd_words_union = rdd_words1.union(rdd_words2)
print("union rdd " + str(rdd_words_union.collect()))

# intersection
rdd_words_intersection = rdd_words1.intersection(rdd_words2)
print("intersection rdd " + str(rdd_words_intersection.collect()))

# subtract
rdd_words_subtract = rdd_words1.subtract(rdd_words2)
print("rdd1 substract rdd2 " + str(rdd_words_subtract.collect()))

# cartesian
rdd_words_cartesian = rdd_words1.cartesian(rdd_words2)
print("rdd1 cartesian rdd2 " + str(rdd_words_cartesian.collect()))
print("length of rdd1 cartesian rdd2 " +
      str(len(rdd_words_cartesian.collect())))
