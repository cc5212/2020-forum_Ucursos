# 2020-forum-ucursos
Analysis of the common words and the feelings associated to them, used in fcfm and Universidad de Chile forums during 3 periods of time
- Before 18O
- Between 18O and start of quarantine in Santiago
- After the start of quarantine to today

Analysis of the most frequent co-stars in IMDb with Hadoop. [Alice Aardvark, Bob Bobcat, Carol Chimera. Group 42]

# Overview
The main goal of this project is to analyze if there is a noticeable change in the common words and in the feelings represented by those words used by participants of the fcfm and Uchile forums in the ucursos platform during the 2 events that marked recent chilean and world's history, the 18O political movement and the COVID-19 pandemic.

State what is the main goal of the project. State what sorts of question(s) you want to answer or what sort of system you want to build. (Questions may be non-technical -- e.g., is there a global correlation between coffee consumption and research output -- so long as they require data analysis or other technical solutions.)

# Data
The data used comes from a scrapping of both of the forums using python, the data is in JSON format and contains the title, date of posting, theme, and content if it's a parent post, and title of parent post, date of posting and content if it's an answer to a post. There is a total of 40MB of lines, and arround 140k unique posts and answers.

Describe the raw dataset that you considered for your project. Where did it come from? Why was it chosen? What information does it contain? What format was it in? What size was it? How many lines/records? Provide links.

# Methods
The analisis of the data was made using map/reduce for word counting in the periods mentioned above, and then that data was used as an input for a pig script that let us associate words with feelings.

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

# Conclusion
After the analisis was done, we can conclude that the fcfm forum did not have a noticeable change during the 18O and COVID events, instead, the behaviour and words used stayed constant
Summarise main lessons learnt. What was easy? What was difficult? What could have been done better or more efficiently?

# Appendix

You can use this for key code snippets that you don't want to clutter the main text.
