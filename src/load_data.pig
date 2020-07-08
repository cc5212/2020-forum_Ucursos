posts = LOAD 'hdfs://cm:9000/uhadoop2020/g10/fcfm_flatten2.json' USING JsonLoader(json:map[]);

b = FOREACH a GENERATE flatten(json#'title') AS title,
                       flatten(json#'date') AS date,
                       flatten(json#'text') AS text,
                       flatten(json#'post_theme') AS post_theme;

DUMP b;