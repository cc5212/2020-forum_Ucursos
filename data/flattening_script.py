# author: {Francisca Suárez}

import json

# abriendo y cerrando json original para lectura
a_file = open("fcfm_final.json", "r", encoding="utf8")
json_object = json.load(a_file)
a_file.close()

result_json = '{"posts": []}'  # new json file that will contain all posts
json_object_writing = json.loads(result_json)

#  matching fields for parents and children
for pages in json_object:
    for padres in json_object[pages]:
        # next line must be uncommented for general forum
        # padres['topic'] = padres.pop('post_theme', None)# renaming the fields
        padres['date'] = padres.pop('date_theme', None)# renaming the fields
        padres['text'] = padres.pop('text_theme', None)# renaming the fields
        json_object_writing["posts"].append(padres)
        if padres["child_theme"] == None:
            None
        else:
            for hijos in padres["child_theme"]:
                hijos['date'] = hijos.pop('date_child', None)# renaming the fields
                hijos['text'] = hijos.pop('text_child', None)# renaming the fields
                hijos["title"] = padres["title"]
                # next line must be uncommented for general forum
                # hijos["topic"] = padres["topic"]
                json_object_writing["posts"].append(hijos)  # adding the childs to posts
                padres.pop('child_theme', None)  # deleting the child field from parent



# abriendo y cerrando json para escritura
a_file = open("fcfm_flatten2.json", "w")
json.dump(json_object_writing, a_file, indent=1)

a_file.close()
