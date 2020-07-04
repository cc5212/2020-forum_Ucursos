# author: {Francisca Suárez}
import json

format = "\t\t  \t\t\tResponder  \t\t\tPadre \t\t\tIgnorar \t\t\t Compartir \t\t\tCerrar"
format_2 = "\t\t   \t\t\tIgnorar \t\t\t Compartir \t\t\tCerrar"
format_3 = "\t\t"
def cero(text):
    if int(text)<10:
        return "0"+text
    else:
        return text
def mesNum(dia,mes):
    if mes == "Enero":
        return cero(dia) + "/" + "01" + "/" + "20"
    elif mes == "Febrero":
        return cero(dia) + "/" + "02" + "/" + "20"
    elif mes == "Marzo":
        return cero(dia) + "/" + "03" + "/" + "20"
    elif mes == "Abril":
        return cero(dia) + "/" + "04" + "/" + "20"
    elif mes == "Mayo":
        return cero(dia) + "/" + "05" + "/" + "20"
    elif mes == "Junio":
        return cero(dia) + "/" + "06" + "/" + "20"
    elif mes == "Julio":
        return cero(dia) + "/" + "07" + "/" + "20"
    elif mes == "Agosto":
        return cero(dia) + "/" + "08" + "/" + "20"
    elif mes == "Septiembre":
        return cero(dia) + "/" + "09" + "/" + "20"
    elif mes == "Octubre":
        return cero(dia) + "/" + "10" + "/" + "20"
    elif mes == "Noviembre":
        return cero(dia) + "/" + "11" + "/" + "20"
    elif mes == "Diciembre":
        return cero(dia) + "/" + "12" + "/" + "20"

def dateFormat(text):
    text_split=text.split(" ")
    if text_split[0] == "Hoy,":
        return "12/06/20"
    elif text_split[0] == "Ayer,":
        return "11/06/20"
    elif text_split[0] == "Lunes" or text_split[0] == "Martes" or text_split[0] == "Miércoles" or text_split[0] == "Jueves" or text_split[0] == "Viernes" or text_split[0] == "Sábado" or text_split[0] == "Domingo":
        return mesNum(text_split[1],text_split[3])
    elif text_split[1] == "de":
        return mesNum(text_split[0],text_split[2])
    else: return text_split[0]

#abriendo y cerrando json para lectura
a_file = open("fcfm.json", "r", encoding="utf8")
json_object = json.load(a_file)
a_file.close()


for pages in json_object:
    for padres in json_object[pages]:
        texto_p = padres["text_theme"]
        texto_limpio_1_p = texto_p.replace(format, '')
        texto_limpio_2_p = texto_limpio_1_p.replace(format_2, '')
        texto_limpio_3_p = texto_limpio_2_p.replace(format_3, '')
        texto_limpio_4_p = texto_limpio_3_p.replace("\t", '')

        padres["text_theme"] = texto_limpio_4_p

        fecha_padre = padres["date_theme"]
        fecha_padre_formato = dateFormat(fecha_padre)
        padres["date_theme"]=fecha_padre_formato
        if padres["child_theme"]==None:
            None
        else:
            for hijos in padres["child_theme"]:
                texto = hijos["text_child"]
                texto_limpio_1=texto.replace(format,'')
                texto_limpio_2 = texto_limpio_1.replace(format_2, '')
                texto_limpio_3 = texto_limpio_2.replace(format_3, '')
                texto_limpio_4 = texto_limpio_3.replace("\t", '')

                hijos["text_child"]=texto_limpio_3
                fecha=hijos["date_child"]
                fecha_formato = dateFormat(fecha)
                hijos["date_child"] = fecha_formato



#abriendo y cerrando json para escritura

a_file = open("fcfm_out.json", "w")

json.dump(json_object, a_file)

a_file.close()
