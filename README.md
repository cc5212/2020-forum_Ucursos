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

Describe the raw dataset that you considered for your project. Where did it come from? Why was it chosen? What information does it contain? What format was it in? What size was it? How many lines/records? Provide links.

# Methods
The analysis of the data was made using map/reduce for word counting in the periods mentioned above, and then that data was used as an input for a pig script that let us associate words with feelings.

Detail the methods used during the project. Provide an overview of the techniques/technologies used, why you used them and how you used them. Refer to the source-code delivered with the project. Describe any problems you encountered.

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



# Conclusion

After the analysis was done, we can conclude that the FCFM forum did not have a noticeable change during the 18O and COVID events, instead, the behavior and words used stayed constant
Summaries main lessons learnt. What was easy? What was difficult? What could have been done better or more efficiently?

# Appendix

You can use this for key code snippets that you don't want to clutter the main text.
