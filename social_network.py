import itertools
import csv
import networkx as nx

#load Chinese
f = open('Chinese_re.csv','r')
recipe_data_ch = list()
for line in csv.reader(f):
       recipe_data_ch.append(line)
f.close()

for i in range(0,len(recipe_data_ch)):
    recipe_data_ch[i].pop(0)
    recipe_data_ch[i]=list(set(recipe_data_ch[i]))
    recipe_data_ch[i].sort()

#load German
f = open('German_re.csv','r')
recipe_data_ge = list()
for line in csv.reader(f):
       recipe_data_ge.append(line)
f.close()

for i in range(0,len(recipe_data_ge)):
    recipe_data_ge[i].pop(0)
    recipe_data_ge[i]=list(set(recipe_data_ge[i]))
    recipe_data_ge[i].sort()
    
#load Italian
f = open('Italian_re.csv','r')
recipe_data_it = list()
for line in csv.reader(f):
       recipe_data_it.append(line)
f.close()

for i in range(0,len(recipe_data_it)):
    recipe_data_it[i].pop(0)
    recipe_data_it[i]=list(set(recipe_data_it[i]))
    recipe_data_it[i].sort()

#load Japanese
f = open('Japanese_re.csv','r')
recipe_data_jap = list()
for line in csv.reader(f):
       recipe_data_jap.append(line)
f.close()

for i in range(0,len(recipe_data_jap)):
    recipe_data_jap[i].pop(0)
    recipe_data_jap[i]=list(set(recipe_data_jap[i]))
    recipe_data_jap[i].sort()

#load Spanish
f = open('Spanish_re.csv','r')
recipe_data_spa = list()
for line in csv.reader(f):
       recipe_data_spa.append(line)
f.close()

for i in range(0,len(recipe_data_spa)):
    recipe_data_spa[i].pop(0)
    recipe_data_spa[i]=list(set(recipe_data_spa[i]))
    recipe_data_spa[i].sort()

#load Thai
f = open('Thai_re.csv','r')
recipe_data_th = list()
for line in csv.reader(f):
       recipe_data_th.append(line)
f.close()

for i in range(0,len(recipe_data_th)):
    recipe_data_th[i].pop(0)
    recipe_data_th[i]=list(set(recipe_data_th[i]))
    recipe_data_th[i].sort()

print "----------------------load data finish-------------------"

combi_data = []
for i in range(0,len(recipe_data_ch)):
    combi_data +=(list(itertools.combinations(recipe_data_ch[i],2)))
for i in range(0,len(recipe_data_ge)):
    combi_data +=(list(itertools.combinations(recipe_data_ge[i],2)))
for i in range(0,len(recipe_data_it)):
    combi_data +=(list(itertools.combinations(recipe_data_it[i],2)))
for i in range(0,len(recipe_data_jap)):
    combi_data +=(list(itertools.combinations(recipe_data_jap[i],2)))
for i in range(0,len(recipe_data_spa)):
    combi_data +=(list(itertools.combinations(recipe_data_spa[i],2)))
for i in range(0,len(recipe_data_th)):
    combi_data +=(list(itertools.combinations(recipe_data_th[i],2)))



print "combi_data length : %d" % (len(combi_data))
print "---------------------data combine finish--------------------"

#print combi_data[0][0]
combi_data.sort()
count = list()
number = 1
edge_data = list(set(combi_data))
print "edge length : %d"%(len(edge_data))
for item in edge_data:
    if (number % 1000 ==0):
        print "1000 data already done"
        number = 0
    count.append(combi_data.count(item))
    number = number + 1

#for i in range(0,len(combi_data)):
#    for j in range(0,len(combi_data[i])):
#        str_com = combi_data[i][j][0]+combi_data[i][j][1]
#        print str_com

G = nx.Graph()
for i in range(0,len(edge_data)):
    G.add_edge(edge_data[i][0],edge_data[i][1],weight=count[i])
    
print len(G.edges())
