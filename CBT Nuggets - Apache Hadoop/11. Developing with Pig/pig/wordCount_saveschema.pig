month2017_11 = LOAD 'hdfs:/user/hadoopuser/csvmanual1year/2017_11.csv' USING PigStorage(',') AS (Ctfb:int,	SessionID:long,	StartDate:datetime,	ProcessDate:datetime,	MonthYearNumber:chararray,	MonthYear:chararray,	YearWeek:chararray,	YearQuarter:chararray,	UUID:chararray,	Country:chararray,	Region:chararray,	Lang:chararray,	Comments:chararray,	HPSAVersion:chararray,	YesNo:chararray,	SubResponse:chararray,	Context:chararray,	SubContext:chararray,	Type:chararray,	OS:chararray,	OSEdition:chararray,	Product:chararray,	PL:chararray);

Store month2017_11 into 'hdfs:/user/hadoopuser/csvmanual1year/schema' USING PigStorage(',', '-schema');
hadoop fs -cp csvmanual1year/schema/.pig_schema csvmanual1year/

just get the schema.
the data is too long.
