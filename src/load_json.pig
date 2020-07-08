posts = LOAD 'hdfs://cm:9000/uhadoop2020/g10/fcfm_flatten.json' USING JsonLoader('title: chararray, post_theme: chararray, date: chararray, text: chararray');

b = LIMIT posts 5;

DUMP b;