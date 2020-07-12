# -*- coding: utf-8 -*-
import csv

files = ["before_18O_sorted.tsv", "18O_covid_sorted.tsv" ,"covid_today_sorted.tsv"]

result = []
for file in files:
	dic = {}
	with open(file) as tsv:
	    i=0
	    print(f"\n{file}:")
	    for line in csv.reader(tsv, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
	        word = line[0]
	        size = line[1]
	        if(len(word)>7):
	        	dic[word] = size
	        	i+=1
	        	if(i>10): break
	result.append(dic)

with open("gt_7.txt", "+w") as txt:
	for i in range(len(files)):
		dic = result[i]
		txt.write(f"{files[i]}:\n")
		for k,v in dic.items():
			txt.write(f"{k}\t{v}\n")
		txt.write("\n")
	txt.close()