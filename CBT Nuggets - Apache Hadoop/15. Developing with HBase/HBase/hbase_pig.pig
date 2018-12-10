movie_data = LOAD 'hdfs:/user/hadoopuser/ml-latest/movies_nocomma.csv' USING PigStorage(',') AS (movieId:int, movieTitle:chararray, genres:chararray);
final_data = FOREACH movie_data generate (int)$0 as movieId, (chararray)$1 as movieTitle;
STORE final_data into 'hbase://movies' USING org.apache.pig.backend.hadoop.hbase.HBaseStorage('movieInfo:movieId,movieInfo:movieTitle');

--Details at logfile: /usr/local/hadoop/hadoop-2.8.5/logs/pig_1544260184854.log
--The first line will casue this much problem?
--the comma is very important