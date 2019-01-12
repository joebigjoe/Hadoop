from pyspark import SparkConf, SparkContext
import os

conf = SparkConf().setMaster("local").setAppName("Get Average Friend By Age")
sc = SparkContext(conf=conf)

# this is an improvement
# since we made a new function to pass to the map function
def processline(line):
    age = int(line.split(",")[2])
    friends = int(line.split(",")[3])
    return (age, friends)

# this is the main area for running the code
path_friends_csv = os.getcwd() + "/fakefriends.csv"
rdd_lines = sc.textFile(path_friends_csv)

# just get the age and the friend
rdd_age_friends = rdd_lines.map(processline)
#print(rdd_age_friends.collect())

# do the compute step 1
rdd_t1 = rdd_age_friends.mapValues(lambda x: (x, 1))
#print(rdd_t1.collect())

# do the compute step 2
rdd_t2 = rdd_t1.reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1]))
#print(rdd_t2.collect())

# do the compute step 3
rdd_t3 = rdd_t2.mapValues(lambda x: x[0]/x[1])
print(rdd_t3.collect())