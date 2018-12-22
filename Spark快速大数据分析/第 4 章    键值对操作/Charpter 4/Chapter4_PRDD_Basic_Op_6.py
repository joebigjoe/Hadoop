from pyspark import SparkConf, SparkContext
import os

# get a local sc
conf = SparkConf().setMaster("local").setAppName("paired RDD with movies")
sc = SparkContext(conf=conf)

# get the movie data
path_movie_data = os.getcwd() + "/movies10.csv"
with(open(path_movie_data)) as f:
    lines_movies = f.readlines()
lines_movies = [x.strip() for x in lines_movies]

rdd_movies = sc.parallelize(lines_movies)
rdd_movies_with_key = rdd_movies.map(lambda token: (token.split(',')[0], token.split(',')[1]))
#print(rdd_movies_with_key.sortByKey(ascending=True).collect())

# get the rating data
path_ratings_data = os.getcwd() + "/ratings10.txt"
with(open(path_ratings_data)) as f:
    lines_ratings = f.readlines()
lines_ratings = [x.strip() for x in lines_ratings]

rdd_ratings = sc.parallelize(lines_ratings)
rdd_ratings_with_movieidaskey = rdd_ratings.map(lambda token: (token.split(',')[1], (token.split(',')[0],token.split(',')[2])))
#print(rdd_ratings_with_movieidaskey.sortByKey(ascending=True).collect())

# join the data
rdd_joined = rdd_movies_with_key.join(rdd_ratings_with_movieidaskey)
rdd_sorted = rdd_joined.sortByKey(ascending=True)
print(rdd_sorted.collect())

# some operation 
#print(rdd_sorted.countByKey())
print(rdd_sorted.collectAsMap())
#print(rdd_sorted.lookup('6'))

# terminate the spark context
sc.stop()