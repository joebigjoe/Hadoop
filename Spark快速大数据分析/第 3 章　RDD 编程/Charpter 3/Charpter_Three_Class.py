class Searcher:
    def __init__(self, query):
        self.query = query
    
    def isMatch(self, s):
        return self.query in s

    def GetMatchesFunctionReference(self, rdd):
        # in the isMatch method, we pass self.query.
        # which means in the rdd.filter, we will also use self.query.
        # which will serialize the whome self class.
        # which is the whole SearchFunctions class.
        # which clould be BIIIIG
        return rdd.filter(self.isMatch)
    
    def GetMatchesMemberReference(self, rdd):
        return rdd.filter(lambda x: self.query in x)

    def GetMatchesMemberReference_better(self, rdd):
        query = self.query
        # this way we will not pass the whole project to the filer method
        return rdd.filter(lambda x: query in x)
    
    def isMatch_better(self, s):
        query = self.query
        # this way we will not pass the whole project to the filer method
        return query in s

import os
from pyspark import SparkConf, SparkContext

# load the data to search 
conf = SparkConf().setMaster("local").setAppName("Word Count With Class")
sc = SparkContext(conf = conf)
filePath = os.getcwd() + "/BoxOfficeMojo.txt"
rdd_lines = sc.textFile(filePath)

# search the lines that associate with Aquaman 
searcher_aquaman = Searcher("Aquaman")
rdd_aquaman = searcher_aquaman.GetMatchesFunctionReference(rdd_lines)
print(rdd_aquaman.first())

# search the lines that associate with Spider-Man
searcher_spider_man = Searcher("Spider-Man")
rdd_spiddy = searcher_spider_man.GetMatchesMemberReference(rdd_lines)
print(rdd_spiddy.first())

# stop the sc
sc.stop()