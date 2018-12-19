from pyspark import SparkConf, SparkContext

# initialize local sc
conf = SparkConf().setMaster("local").setAppName("Spark Basic Opreation")
sc = SparkContext(conf=conf)

# test map
numbers = [1, 2, 3, 4, 5]
rdd_numbers = sc.parallelize(numbers)
rdd_numbers = rdd_numbers.map(lambda x: x*x)
list_numbers_squared = rdd_numbers.collect()
print(list_numbers_squared)

# test filter
rdd_numbers_biggerthan10 = rdd_numbers.filter(lambda x: x > 10)
list_numbers_biggerthan10 = rdd_numbers_biggerthan10.collect()
print(list_numbers_biggerthan10)

# test flatmap
# from the name we can see it has 2 steps, flat and map
dialogs = ["When you play the game of thrones, you win or you die. There is no middle ground.", "There are no men like me, There's only me.",
           "When the snows fall and the white winds blow, the lone wolf dies but the pack survives.", "What is dead may never die, but rises again, harder and stronger."]
rdd_dialogs = sc.parallelize(dialogs)
rdd_words = rdd_dialogs.flatMap(lambda x: x.split(" "))
list_words = rdd_words.collect()
print(list_words)

 
sc.stop()