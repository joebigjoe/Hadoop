-- load the data
-- use .pig_schema only when all the files in the folder is using the same schema
movies = LOAD 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/movies.csv' USING PigStorage(',') AS (movieId:int, title:chararray, genres:chararray);
ratings = LOAD 'hdfs:/user/hadoopuser/moviedata/ml-latest-small/ratings.csv' USING PigStorage(',') AS (userId:int, movieId:int, rating:int, timestamp:chararray);

-- filter the data and test a small sample
movies_100 = FILTER movies BY movieId <= 100;
--dump movies_100;
ratings_100 = FILTER ratings BY userId <= 100;
--dump ratings_100;

-- join movies_100 and raings_100
-- when inner join have exceptions. think of OUTER Connect.
join_100 = JOIN ratings_100 BY movieId LEFT OUTER, movies_100 BY movieId;
-- describe is very useful. that is how i found out to use ratings_100::userId, NOT ratings_100.userId
-- there is huge difference after join and group, when access their parameters.
describe join_100;

-- get the movies which has been rated by userId == 1
join_100_1 = FILTER join_100 BY ratings_100::userId == 1;

-- dump to see the result
--dump join_100_1;
--describe join_100_1;
/* {ratings_100::userId: int,ratings_100::movieId: int,ratings_100::rating: int,ratings_100::timestamp: chararray,movies_100::movieId: int,movies_100::title: chararray,movies_100::genres: chararray}
*/

-- get the genres that the user likes and order them by count
join_100_1_genres = FILTER join_100_1 BY NOT movies_100::genres == NULL;
/*
(1,1,4,964982703,1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy)
(1,3,4,964981247,3,Grumpier Old Men (1995),Comedy|Romance)
(1,6,4,964982224,6,Heat (1995),Action|Crime|Thriller)
(1,47,5,964983815,47,Seven (a.k.a. Se7en) (1995),Mystery|Thriller)
(1,50,5,964982931,50,"Usual Suspects, The (1995)")
(1,70,3,964982400,70,From Dusk Till Dawn (1996),Action|Comedy|Horror|Thriller)
*/

genres =  FOREACH join_100_1_genres GENERATE STRSPLIT(movies_100::genres, '\\|', -1) as words;
dump genres;
/*
((Adventure,Animation,Children,Comedy,Fantasy))
((Comedy,Romance))
((Action,Crime,Thriller))
((Mystery,Thriller))
(( The (1995)"))
((Action,Comedy,Horror,Thriller))
*/

describe genres;
/* genres: {words: ()} */

genres_flattened =  FOREACH join_100_1_genres GENERATE FLATTEN(STRSPLIT(movies_100::genres, '\\|', -1)) as words;
dump genres_flattened;
/*
(Adventure,Animation,Children,Comedy,Fantasy)
(Comedy,Romance)
(Action,Crime,Thriller)
(Mystery,Thriller)
( The (1995)")
(Action,Comedy,Horror,Thriller)
*/
describe genres_flattened;
-- genres_flattened: {words: bytearray}

genres_flattened_tokenized = FOREACH genres_flattened GENERATE TOKENIZE(words) as words_tokenized;
dump genres_flattened_tokenized;
/*
(Adventure)
(Comedy)
(Action)
(Mystery)
( The (1995)")
(Action)
*/