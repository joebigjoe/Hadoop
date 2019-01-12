from pyspark import SparkConf, SparkContext
import os

# set the spark context
# Master must either be yarn or start with spark, mesos, k8s, or local
# and it is case senstive
conf = SparkConf().setMaster("local").setAppName("Lowest Temp")
sc = SparkContext(conf=conf)

# a function to process line.
def processLine(line):
    feilds = line.split(",")
    station = feilds[0]
    type_ = feilds[2]
    temp = float(feilds[3]) * 0.1 * 1.8 + 32.0
    return (station, type_, temp)

# this is the start point for all the code
path_1800_csv = os.getcwd() + "/1800.csv"
rdd_lines = sc.textFile(path_1800_csv)
rdd_shrinked = rdd_lines.map(processLine)
rdd_filtered = rdd_shrinked.filter(lambda x: x[1] == "TMAX")
rdd_min_list = rdd_filtered.map(lambda x: (x[0], x[2]))
rdd_min = rdd_min_list.reduceByKey(lambda x, y: max(x,y))
print(rdd_min.collect())