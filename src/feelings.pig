-- This script returns the sum of all the times that a word associated with an emotion was used in the forum.
-- For this, a table that classifies Spanish words into feelings was used (source: http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm), giving them a value of 1 if such feeling is perceived from the word, and 0 if not.
-- The sentiments that this table contains are negative and positive. The emotions are: anger, anticipation, disgust, fear, joy, sadness, surprise, and trust.

--CHANGE THE NEXT FILE TO ANALYZE DIFFERENT DATA
--words = LOAD 'hdfs://cm:9000/uhadoop2020/fsuarez/word_count_sorted_no_diacritics.tsv' USING PigStorage('\t') AS (word:chararray, count:int);
--words = LOAD 'hdfs://cm:9000/uhadoop2020/fsuarez/before_18O_sorted_no_diacritics.tsv' USING PigStorage('\t') AS (word:chararray, count:int);
words = LOAD 'hdfs://cm:9000/uhadoop2020/fsuarez/18O_covid_sorted_no_diacritics.tsv' USING PigStorage('\t') AS (word:chararray, count:int);
--words = LOAD 'hdfs://cm:9000/uhadoop2020/fsuarez/covid_today_sorted_no_diacritics.tsv' USING PigStorage('\t') AS (word:chararray, count:int);


feelings = LOAD 'hdfs://cm:9000/uhadoop2020/fsuarez/feelings_no_diacritics.tsv' USING PigStorage('\t') AS 
	(word:chararray, positive:int, negative:int, anger:int, anticipation:int, disgust:int, fear:int, joy:int, sadness:int, surprise:int, trust:int);

-- Because we had to normalize diacritics, some words are duplicated now, we will merge all those instances

unique_words = GROUP words BY word;

no_duplicates = foreach unique_words generate group, SUM(words.count);

-- Now we join both tables, the one with the words used in the forum and its counter, and the word associated to the feelings with its counters.
result = JOIN no_duplicates by $0 LEFT OUTER, feelings by word;

-- Cleaning rows without a match (no associated feeling word)
filter_data = FILTER result BY($2 is not null);

result_group = GROUP filter_data BY ($0, $1, $2);

-- Again, we clean duplicates from the join
filtered = FOREACH result_group {
      one_record = LIMIT filter_data 1;
      GENERATE FLATTEN(one_record);
};

-- Renaming attributes for better organisation
renamed = foreach filtered generate $0 as wordA, $1 as number,$2 as wordB, $3 as positive, $4 as negative, 
	$5 as anger, $6 as anticipation,$7 as disgust, $8 as fear, $9 as joy, $10 as sadness, $11 as surprise, $12 as trust;

-- Multiplying the number of appereances of a word related to a feeling in the forum, to the indicators on each feeling
multiplied_feelings = FOREACH renamed GENERATE 
	number*positive as positive,
	number*negative as negative, 
	number*anger as anger, 
	number*anticipation as anticipation, 
	number*disgust as disgust, 
	number*fear as fear,
	number*joy as joy,
	number*sadness as sadness,
	number*surprise as surprise,
	number*trust as trust;

-- Adding each column obtaining the total value per feeling
summary = GROUP multiplied_feelings ALL;
result = FOREACH summary GENERATE 
	SUM(multiplied_feelings.positive),
	SUM(multiplied_feelings.negative),
	SUM(multiplied_feelings.anger),
	SUM(multiplied_feelings.anticipation),
	SUM(multiplied_feelings.disgust),
	SUM(multiplied_feelings.fear),
	SUM(multiplied_feelings.joy),
	SUM(multiplied_feelings.sadness),
	SUM(multiplied_feelings.surprise),
	SUM(multiplied_feelings.trust);


-- output  for the final count

STORE result INTO '/uhadoop2020/fsuarez/3/';



