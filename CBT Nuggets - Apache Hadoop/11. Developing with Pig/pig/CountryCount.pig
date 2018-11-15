-- load all the data for the latest one year.
month2017_11 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2017_11.csv' USING PigStorage(',');
month2017_12 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2017_12.csv' USING PigStorage(',');
month2018_01 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_01.csv' USING PigStorage(',');
month2018_02 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_02.csv' USING PigStorage(',');
month2018_03 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_03.csv' USING PigStorage(',');
month2018_04 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_04.csv' USING PigStorage(',');
month2018_05 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_05.csv' USING PigStorage(',');
month2018_06 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_06.csv' USING PigStorage(',');
month2018_07 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_07.csv' USING PigStorage(',');
month2018_08 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_08.csv' USING PigStorage(',');
month2018_09 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_09.csv' USING PigStorage(',');
month2018_10 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2018_10.csv' USING PigStorage(',');

-- union the data to ONE big file
yearone = UNION month2017_11, month2017_12, month2018_01, month2018_02, month2018_03, month2018_04, month2018_05, month2018_06, month2018_07, month2018_08, month2018_09, month2018_10;

-- dump the shit to the screen
-- dump yearone;

-- in the last line of the pig run. 
-- you will see the time comsumed.
-- org.apache.pig.Main - Pig script completed in 1 minute, 56 seconds and 381 milliseconds (116381 ms)

-- split by location
SPLIT yearone INTO
	yearone_AMERICAS IF Region == 'AMERICAS',
	yearone_EMEA IF Region == 'EMEA',
	yearone_ASIAPACIFIC IF Region == 'ASIA PACIFIC';

-- dump ASIA PACIFIC
-- dump yearone_ASIAPACIFIC

-- group ASIA PACIFIC by country and then check what country has the most search 
yearone_ASIAPACIFIC_Grouped_By_Country = GROUP yearone BY Country;

-- dump to see the info 
-- dump yearone_ASIAPACIFIC_Grouped_By_Country;

-- count by country
yearone_ASIAPACIFIC_Count_By_Country = FOREACH yearone_ASIAPACIFIC_Grouped_By_Country GENERATE group, COUNT(yearone.UUID) as numberOfSearch;

-- dump yearone_ASIAPACIFIC_Count_By_Country
-- dump yearone_ASIAPACIFIC_Count_By_Country;

-- order by numberOfSearch
yearone_ASIAPACIFIC_Count_By_Country_Ordered = ORDER yearone_ASIAPACIFIC_Count_By_Country by numberOfSearch DESC;

-- dumpit
dump yearone_ASIAPACIFIC_Count_By_Country_Ordered;

