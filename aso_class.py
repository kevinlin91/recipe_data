import csv
#category 0: Chinese , 1:German , 2:Italian , 3:Japanese , 4: Spanish , 5: Thai
#you need to modify line22 37 38 56
def search(name, food_data):
    number=-1
    for i in range(0,len(food_data)):
        if name == food_data[i][0]:
          number = i  

    return number




#read total food
f = open('./idf/total_idf.csv','r')
food_data = list()
for line in csv.reader(f):
    food_data.append(line)
f.close()
#read recipe
f = open('Thai_re.csv','r')
recipe_data = list()
for line in csv.reader(f):
       recipe_data.append(line)
f.close()
food_data.sort()

#test search method
#print search(recipe_data[0][4],food_data)
for i in range(0,len(recipe_data)):
    recipe_data[i].pop(0)
    recipe_data[i]=list(set(recipe_data[i]))
    recipe_data[i].sort()


count = 11889
str_ac = "CLASS=5 "
str_total = ""
length = len(food_data)

for i in range(0,len(recipe_data)):
    food_list = [0] * length
    for j in range(0,len(recipe_data[i])):
        food_list[search(recipe_data[i][j],food_data)] = 1       
        #str_svm += str(search(recipe_data[i][j],food_data)) + ":" + "1"+ " "
        
    str_total += str(count) + " " + str_ac
    for k in range(0,length):
        str_total += "w[" + str(k) + "]=" + str(food_list[k]) + " "

    count = count + 1
    str_total += "\n"
    print "recipe",i,"done"

fp = open('Thai','w')
fp.write(str_total)
fp.close()
    
