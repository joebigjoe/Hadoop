from pyspark import SparkConf, SparkContext

# initialize local sc
conf = SparkConf().setMaster("local").setAppName("Spark Basic Opreation")
sc = SparkContext(conf=conf)

# test set 1
dialogs1 = ["Apple Apple apple cabage banana pear tomato"]
rdd_dialogs1 = sc.parallelize(dialogs1)
rdd_words1 = rdd_dialogs1.flatMap(lambda x: x.split(" "))
print(rdd_words1.sample(False, 0.1).collect())
print(rdd_words1.sample(False, 0.2).collect())
print(rdd_words1.sample(False, 0.3).collect())
print(rdd_words1.sample(False, 1).collect())
print(rdd_words1.sample(False, 2).collect())
print(rdd_words1.sample(False, 3).collect())
