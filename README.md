# 2020-forum-ucursos
Análisis de las palabras más comunes y los sentimientos asociados a ellos dentro del foro de la FCFM de la Universidad de Chile, durante 3 periodos de tiempo:

- Antes del 18 de Octubre (estallido social de Chile)
- Entre el 18 de Octubre y el comienzo de la cuarentena debido al Covid-19 en Santiago de Chile
- Desde el comienzo de la cuarentena en Santiago de Chile hasta hoy

# Resumen
El principal objetivo de este proyecto es analizar si hay un cambio notable en las palabras comunes y en los sentimientos representados por las palabras usadas por los participantes del foro de la FCFM en la plataforma [ucursos](http://ucursos.cl/) durante los 2 eventos que han marcado significativamente la historia de Chile y el mundo, el **estallido social** del 18 de Octubre del 2019 y la pandemia mundial del COVID-19.

Las preguntas que se esperan resolver son las siguientes:

1.  ¿Cuales son las palabras más populares presentes en los comentarios del foro?
2.  ¿Cómo afectó el estallido social y el inicio de la cuarentena en las palabras usadas dentro del foro?
3.  ¿Existe una correlación entre las palabras más comunes y las fechas importantes de revuelo nacional e internacional?
4.  ¿Existe una mayor participación dentro del foro en fechas relevantes?

# Data
El dataset principal fue obtenido por medio de un web scraping realizado dentro del foro de ucursos usando la gema `Watir` en Ruby. Los datos fueron tratados realizando una limpieza en Python y se almacenaron en un archivo TSV para el trabajo con Hadoop. Cada fila del dataset usado contiene los siguientes datos:

* `Title`: Titulo del post. Si es un comentario entonces contiene el titulo del post.
* `Date of posting`: Fecha de publicación de cada post y comentario.
* `Theme of post`: Tema del post. Si es un comentario del post principal este dato está en nulo.
* `Content`: Contenido del post o comentario

El tamaño del dataset es de **40 MB** y posee alrededor de **140k** tuplas 

El segundo dataset con el que se trabajó fue **[NRC Sentiment Lexicons](http://saifmohammad.com/)** el que contiene un conjunto de palabras traducidas al español donde clasifica los sentimientos de cada una: (anger, anticipation, disgust, fear, joy, sadness, surprise, trust)

El tamaño del dataset es de **190 KB** su formato es **TSV** y posee **6356** tuplas

Se escogió este dataset debido a que se quería estudiar los sentimientos de los estudiantes de la FCFM en los comentarios que se postearon en el foro en fechas importantes.

# Métodos
El análisis de los datos se realizó en Java Hadoop, utilizando MapReduce para el recuento de palabras en los períodos mencionados anteriormente, y luego esos datos se utilizaron como entrada para un script en Pig que nos permitió asociar palabras con sentimientos.

La tabla que contenía las palabras y los sentimientos asociados a ellas, era una traducción proveida por su creador, pero habían muchas palabras sin traducción, o su traducción era de dos palabras o más (por lo tanto, en nuestro análisis no servirían). Es por esto que hubo que eliminar varias de sus tuplas. 

Además, las tildes también fueron un problema, puesto que en el foro no siempre se utilizan las palabras tildadas, por lo que hubo que normalizar estos símbolos tanto como para la tabla de emociones, como para la de nuestros datos. Tomamos en cuenta que podría haber malentendidos entre palabras que se tildan de forma distinta y expresan sentimientos opuestos, pero considerando la cantidad de datos perdidos en el join si se mantenían las tildes, preferimos normalizar los datasets.


# Results
After analyzing the data, it became clear that there was not a noticeable change in the number of words associated to a certain feeling in any given period, if anything, we saw the biggest change was the decrease of words associated with negative emotion, but that was only a 2,5% decrease in the number of words.
## Total number of words associated with a feeling by period

|              | Before 18O | 18O-COVID | COVID-TODAY |
|--------------|:----------:|:---------:|:-----------:|
| positive     |   168705   |    7844   |    11570    |
| negative     |    68282   |    3235   |     5921    |
| anger        |    20835   |    1002   |     1485    |
| anticipation |    48270   |    2365   |     3370    |
| disgust      |    15831   |    765    |     1286    |
| fear         |    28734   |    1578   |     2484    |
| joy          |    31910   |    1549   |     1976    |
| sadness      |    38581   |    1856   |     3198    |
| surprise     |    15574   |    756    |     1031    |
| trust        |    86761   |    4124   |     5941    |
| TOTAL        |   523483   |   25074   |    38262    |

This table was then translated to percentages to see the percentage difference by period

|              | Before 18O | 18O-COVID | COVID-TODAY |
|--------------|:----------:|:---------:|:-----------:|
| positive     | 32.22741   | 31.2834   | 30.23888    |
| negative     | 13.04379   | 12.90181  | 15.47488    |
| anger        | 3.980072   | 3.996171  | 3.881135    |
| anticipation | 9.22093    | 9.432081  | 8.807694    |
| disgust      | 3.024167   | 3.050969  | 3.361037    |
| fear         | 5.489003   | 6.293372  | 6.492081    |
| joy          | 6.095709   | 6.177714  | 5.164393    |
| sadness      | 7.370058   | 7.40209   | 8.358162    |
| surprise     | 2.975073   | 3.015075  | 2.694579    |
| trust        | 16.5738    | 16.44732  | 15.52715    |

And finally we can calculate the difference by period

|              | Before 180 ->   18O-COVID | 18O-COVID -> COVID-TODAY |
|--------------|:-------------------------:|:------------------------:|
| positive     |        0.944006443        |        1.044521827       |
| negative     |        0.141974927        |       -2.573073056       |
| anger        |        -0.016099392       |        0.115036003       |
| anticipation |        -0.21115123        |        0.624386722       |
| disgust      |        -0.026802157       |       -0.310067929       |
| fear         |        -0.804368157       |       -0.198709296       |
| joy          |        -0.082005032       |        1.013321096       |
| sadness      |        -0.032031952       |       -0.956072331       |
| surprise     |        -0.040002643       |        0.320495899       |
| trust        |        0.126479193        |        0.920161065       |

Detail the results of the project. Different projects will have different types of results; e.g., run-times or result sizes, evaluation of the methods you're comparing, the interface of the system you've built, and/or some of the results of the data analysis you conducted.



## Dates with most post published

| 21-10-2019 | 261  |
| ---------- | ---- |
| 29-10-2019 | 227  |
| 13-05-2020 | 225  |
| 01-05-2020 | 218  |
| 26-05-2020 | 215  |
| 29-04-2020 | 212  |
| 29-03-2020 | 188  |
| 16-03-2020 | 176  |
| 23-03-2020 | 176  |
| 12-05-2020 | 166  |



![](https://github.com/cc5212/2020-forum_Ucursos/blob/master/images/post_fecha.png)



## Dates with most comments

| 01-05-2020 | 13060 |
| ---------- | ----- |
| 29-10-2019 | 11861 |
| 13-05-2020 | 11807 |
| 23-03-2020 | 9199  |
| 29-03-2020 | 7349  |
| 22-03-2020 | 7266  |
| 29-04-2020 | 6308  |
| 11-04-2020 | 6287  |
| 27-04-2020 | 5848  |
| 06-06-2020 | 5608  |

## Palabras más usadas por periodo
En esta sección las tildes sí fueron consideradas. 
### Palabras de largo igual o mayor a 4
|      Antes 18O |        |     18O-COVID19 |        |        COVID19-HOY |        |
|----------------|--------|-----------------|--------|--------------------|--------|
| Palabra        | Conteo | Palabra         | Conteo | Palabra            | Conteo |
| gracias        | 8823   | gracias         | 332    | clases             | 496    |
| saludos        | 8623   | saludos         | 312    | gracias            | 474    |
| alguien        | 8548   | está            | 303    | hacer              | 468    |
| todos          | 6228   | alguien         | 271    | estudiantes        | 459    |
| tiene          | 5950   | tiene           | 253    | todos              | 408    |
| está           | 5400   | todos           | 214    | también            | 403    |
| facultad       | 4639   | también         | 213    | está               | 400    |
| hacer          | 4441   | porque          | 206    | alguien            | 392    |
| tengo          | 4394   | desde           | 201    | porque             | 381    |
| porque         | 4327   | sobre           | 197    | saludos            | 378    |
| puede          | 4252   | chile           | 195    | tiene              | 375    |
### Palabras de largo igual o mayor a 5
|        Antes 18O |        |       18O-COVID19 |        |       COVID19-HOY |        |
|------------------|--------|-------------------|--------|-------------------|--------|
| Palabra          | Conteo | Palabra           | Conteo | Palabra           | Conteo |
| gracias          | 8823   | gracias           | 332    | clases            | 496    |
| saludos          | 8623   | saludos           | 312    | gracias           | 474    |
| alguien          | 8548   | alguien           | 271    | estudiantes       | 459    |
| facultad         | 4639   | también           | 213    | también           | 403    |
| porque           | 4327   | porque            | 206    | alguien           | 392    |
| también          | 4129   | pueden            | 169    | porque            | 381    |
| pueden           | 3811   | facultad          | 168    | saludos           | 378    |
| cuando           | 3665   | cualquier         | 155    | facultad          | 364    |
| cualquier        | 3641   | están             | 152    | semestre          | 362    |
| estudiantes      | 3199   | estudiantes       | 151    | universidad       | 332    |
| correo           | 3154   | cuando            | 150    | online            | 287    |
### Palabras de largo igual o mayor a 6
|        Antes 18O |        |       18O-COVID19 |        |       COVID19-HOY |        |
|------------------|--------|-------------------|--------|-------------------|--------|
| Palabra          | Conteo | Palabra           | Conteo | Palabra           | Conteo |
| gracias          | 8823   | gracias           | 332    | gracias           | 474    |
| saludos          | 8623   | saludos           | 312    | estudiantes       | 459    |
| alguien          | 8548   | alguien           | 271    | también           | 403    |
| facultad         | 4639   | también           | 213    | alguien           | 392    |
| también          | 4129   | facultad          | 168    | saludos           | 378    |
| cualquier        | 3641   | cualquier         | 155    | facultad          | 364    |
| estudiantes      | 3199   | estudiantes       | 151    | semestre          | 362    |
| beauchef         | 2707   | personas          | 146    | universidad       | 332    |
| facebook         | 2689   | universidad       | 145    | escuela           | 268    |
| universidad      | 2487   | información       | 136    | personas          | 231    |
| además           | 2477   | práctica          | 127    | situación         | 221    |

### Palabras de largo igual o mayor a 7
|        Antes 18O |        |       18O-COVID19 |        |       COVID19-HOY |        |
|------------------|--------|-------------------|--------|-------------------|--------|
| Palabra          | Conteo | Palabra           | Conteo | Palabra           | Conteo |
| facultad         | 4639   | también           | 213    | estudiantes       | 459    |
| también          | 4129   | facultad          | 168    | también           | 403    |
| cualquier        | 3641   | cualquier         | 155    | facultad          | 364    |
| estudiantes      | 3199   | estudiantes       | 151    | semestre          | 362    |
| beauchef         | 2707   | personas          | 146    | universidad       | 332    |
| facebook         | 2689   | universidad       | 145    | personas          | 231    |
| universidad      | 2487   | información       | 136    | situación         | 221    |
| información      | 2322   | práctica          | 127    | comunidad         | 214    |
| semestre         | 2308   | arriendo          | 125    | problemas         | 195    |
| comunidad        | 2290   | departamento      | 123    | problema          | 187    |
| ingeniería       | 2248   | ingeniería        | 112    | respecto          | 172    |

![](https://github.com/cc5212/2020-forum_Ucursos/blob/master/images/com_fecha.png)

# Conclusión

Después de que se realizó el análisis, podemos concluir que el foro FCFM no tuvo un cambio notable durante los eventos 18O y COVID, en cambio, el comportamiento y las palabras utilizadas se mantuvieron constantes. Aunque, modificando el largo de las palabras filtradas, la tónica de la problemática de cada período va apareciendo. Por ejemplo, durante el periodo de 18O-COVID19 encontramos "chile" y en el periodo COVID19-HOY encontramos palabras como "clases", "online", "situación" y "problema/s".

Respecto al conteo de emociones, podemos atribuir este cambio tan pequeño a que la tabla utilizada para ello era una traducción automatizada del inglés, por lo que se pierde mucha información. Por otro lado, el lenguaje chileno tiene varias características particulares que pueden hacer difícil compararlo con una tabla tan general. Otra perspectiva, es que los estudiantes de la facultad mantienen el positivismo frente a situaciones complejas.

