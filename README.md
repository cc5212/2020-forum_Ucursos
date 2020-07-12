# 2019-forum-ucursos
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

Detail the results of the project. Different projects will have different types of results; e.g., run-times or result sizes, evaluation of the methods you're comparing, the interface of the system you've built, and/or some of the results of the data analysis you conducted.

# Conclusion

Summarise main lessons learnt. What was easy? What was difficult? What could have been done better or more efficiently?

# Appendix

You can use this for key code snippets that you don't want to clutter the main text.
