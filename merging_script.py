# author: {Francisca Suárez}

import json

# abriendo y cerrando json original para lectura
a_file = open("fcfm_2019-2014_flat.json", "r", encoding="utf8")
json_object_a = json.load(a_file)
a_file.close()

b_file = open("fcfm_2020-2019_flat.json", "r", encoding="utf8")
json_object_b = json.load(b_file)
b_file.close()

json_object_b["posts"].extend(json_object_a["posts"])  # merging two json files

a_file = open("fcfm_2020-2014_flat.json", "w")
json.dump(json_object_b, a_file, indent=1)

a_file.close()
