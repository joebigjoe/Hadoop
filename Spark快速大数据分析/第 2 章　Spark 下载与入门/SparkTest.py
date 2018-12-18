from pyspark import SparkConf, SparkContext
import os

conf = SparkConf().setMaster('local').setAppName('My App')
sc = SparkContext(conf = conf)

# this is the local file to process
file = os.getcwd() + "/README.md"
print file

# load the file to lines
lines = sc.textFile(file)
print lines.first()

# filtered 
filteredlines = lines.filter(lambda line: "Python" in line)
print filteredlines.first()

#exit the sc
sc.stop()