book = LOAD 'hdfs:///data/small/war_and_peace.txt' USING PigStorage() AS (lines:chararray);
words = FOREACH book GENERATE FLATTEN(TOKENIZE(lines)) as word;
wordsGrouped = GROUP words BY word;
wordsAggregated = FOREACH wordsGrouped GENERATE group as word, COUNt(words);
wordsSorted = SORT wordsAggregated $1 DESC;
store wordsSorted INTO 'hdfs:///data/small/pigresult';
