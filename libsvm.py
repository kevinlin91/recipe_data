import csv
#category 1: Chinese , 2:German , 3:Italian , 4:Japanese , 5: Spanish , 6: Thai

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



str_svm = "6 "
for i in range(0,len(recipe_data)):
    for j in range(1,len(recipe_data[i])):
        str_svm += str(search(recipe_data[i][j],food_data)) + ":" + "1"+ " "
    if( i == len(recipe_data)-1 ):
        str_svm += "\n" 
    else:
        str_svm += "\n" + "6 "
    
fp = open('Thai','w')
fp.write(str_svm)
fp.close()
