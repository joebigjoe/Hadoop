import os
from pyspark import SparkConf, SparkContext

# local sc
conf = SparkConf().setMaster("local").setAppName("basic operation")
sc = SparkContext(conf=conf)

# rdd
list_number = [1, 2, 3, 4, 5]
rdd_number = sc.parallelize(list_number)

# get the sum
rdd_reduced = rdd_number.reduce(lambda x, y: x+y)
print(rdd_reduced)

# get the number of the list
rdd_number_mapped = rdd_number.map(lambda x: 1)
rdd_mapped_reduced = rdd_number_mapped.reduce(lambda x, y: x+y)
print(rdd_mapped_reduced)

# average
average = rdd_reduced/rdd_mapped_reduced
print(average)

# another test
dialogs = ["Can a man still be brave if he's afraid?",
           "That is the only time a man can be brave."]
rdd_dialogs = sc.parallelize(dialogs)
rdd_dialogs_flat = rdd_dialogs.flatMap(lambda dialog: dialog.split(" "))
print(rdd_dialogs_flat.collect())

rdd_dialogs_reduced = rdd_dialogs_flat.reduce(lambda wordx, wordy: wordx + " " + wordy )
print(rdd_dialogs_reduced)