import itertools
import csv
f = open('Test_re.csv','r')
recipe_data = list()
for line in csv.reader(f):
       recipe_data.append(line)
f.close()

for i in range(0,len(recipe_data)):
    recipe_data[i].pop(0)
    recipe_data[i]=list(set(recipe_data[i]))
    recipe_data[i].sort()

combi_data = list()

for i in range(0,len(recipe_data)):
    combi_data.append(list(itertools.combinations(recipe_data[i],2)))

fp = open('Test','w')
for i in range(0,len(combi_data)):
    fp.write(combi_data[i][0]+combi_data[i][1])


fp.close()
