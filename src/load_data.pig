posts = LOAD 'hdfs://cm:9000/uhadoop2020/g10/fcfm_flatten.json' USING JsonLoader() AS (title, post_theme, date, text);

b = LIMIT posts 5;

DUMP b;