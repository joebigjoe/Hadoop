from pyspark import SparkConf, SparkContext
import os

conf = SparkConf().setMaster("local").setAppName("parallelize test")
sc = SparkContext(conf = conf)

list_ = ["game", "of", "thrones"]
words = sc.parallelize(list_)

print words
print words.first()

current_path = os.getcwd() + "/BoxOfficeMojo.txt"
print current_path
linesFromFile = sc.textFile(current_path)

print linesFromFile
print linesFromFile.first()

spiderman = linesFromFile.filter(lambda x : "Spider-Man" in x)
print spiderman.first()

aquaman = linesFromFile.filter(lambda x : "Aquaman" in x)
print aquaman.first()

superheros = spiderman.union(aquaman)
print superheros.count()

for line in superheros.take(5):
    print line

sc.stop()