movie_data = LOAD 'hdfs:/user/hadoopuser/ml-latest/movies_nocomma.csv' USING PigStorage(',') AS (movieId:int, movieTitle:chararray, genres:chararray);
final_data = FOREACH movie_data generate movieId;
STORE final_data into 'hbase://movies' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('movieInfo:movieId');

--Details at logfile: /usr/local/hadoop/hadoop-2.8.5/logs/pig_1544260184854.log
