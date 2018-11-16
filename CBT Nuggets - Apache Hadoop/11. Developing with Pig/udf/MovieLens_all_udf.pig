-- registe the udf jars
REGISTER /home/hadoopuser/pig/CountGenres.jar;

-- load the data
-- use .pig_schema only when all the files in the folder is using the same schema
movies = LOAD 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/movies_nocomma.csv' USING PigStorage(',') AS (movieId:int, title:chararray, genres:chararray);
ratings = LOAD 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/ratings.csv' USING PigStorage(',') AS (userId:int, movieId:int, rating:int, timestamp:chararray);

-- join movies and raings
-- when inner join have exceptions. think of OUTER Connect.
joined = JOIN ratings BY movieId LEFT OUTER, movies BY movieId;
-- describe is very useful. that is how i found out to use ratings::userId, NOT ratings.userId
-- there is huge difference after join and group, when access their parameters.
--describe joined;
--joined: {ratings::userId: int,ratings::movieId: int,ratings::rating: int,ratings::timestamp: chararray,movies::movieId: int,movies::title: chararray,movies::genres: chararray}

--group the joined data by userid
joined_group_by_userid = GROUP joined BY ratings::userId;
--dump joined_group_by_userid;
describe joined_group_by_userid;
/*
{group: int,joined: {(ratings::userId: int,ratings::movieId: int,ratings::rating: int,ratings::timestamp: chararray,movies::movieId: int,movies::title: chararray,movies::genres: chararray)}}
*/

genresforuser = FOREACH joined_group_by_userid {
	genreslist = FOREACH joined GENERATE CONCAT(REPLACE(movies::genres, '\\|', ','), '');
	GENERATE group, genreslist;
};
--dump genresforuser;
describe genresforuser;

/*
genresforuser = FOREACH joined_group_by_userid {
	genreslist = FOREACH joined GENERATE TOKENIZE(CONCAT(REPLACE(movies::genres, '\\|', '*'), '*'));
	GENERATE group, genreslist;
};
--dump genresforuser;
describe genresforuser;
*/


-- bag to string data
genresforuser_bagtostring = FOREACH genresforuser GENERATE group, BagToString(genreslist, ',') as wordsstring;
dump genresforuser_bagtostring;
describe genresforuser_bagtostring;
STORE genresforuser_bagtostring into 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/genresforuser_bagtostring5'; 


/*
-- tuple data
genresforuser_bagtotuple = FOREACH genresforuser GENERATE group, BagToTuple(genreslist) as wordstuple;
dump genresforuser_bagtotuple;
describe genresforuser_bagtotuple;
--STORE genresforuser_bagtotuple into 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/genresforuser_bagtotuple1'; 
*/


-- use udf to deal with tuple and count the genres.
final_data = FOREACH genresforuser_bagtostring GENERATE group, joey.test.CountGenres(wordsstring) as genres;
dump final_data;
describe final_data;
STORE final_data into 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/final_data5';

/*
-- fltten data
genresforuser_flatten = FOREACH genresforuser_bagtotuple GENERATE group, FLATTEN(wordstuple) as wordsfaltten;
--dump genresforuser_flatten;
describe genresforuser_flatten;
--STORE genresforuser_flatten into 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/genresforuser_flatten1'; 

-- flatten replace
genresforuser_flatten_replace = FOREACH genresforuser_flatten GENERATE group, REPLACE(wordsfaltten, '\u0009', ',') as --wordsfalttenreplace;
--dump genresforuser_flatten_replace;
--STORE genresforuser_flatten_replace into 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/genresforuser_flatten_replace1'; 


-- tokenize data
genresforuser_tokenize = FOREACH genresforuser_bagtostring GENERATE group, FLATTEN(TOKENIZE(wordsstring, ',')) as words;
--dump genresforuser_tokenize;
describe genresforuser_tokenize;
--STORE genresforuser_tokenize into 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/genresforuser_tokenize1'; 

-- count the keywords for each user
grouped =  GROUP genresforuser_tokenize by (group, (group, words));
--dump grouped;
describe grouped;

needed =  FOREACH grouped GENERATE group, COUNT(genresforuser_tokenize) as preference;
--dump needed;
describe needed;

ordered = ORDER needed by group, preference DESC;
--dump ordered;
STORE ordered into 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/best_for_now';
*/
