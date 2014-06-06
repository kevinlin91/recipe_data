import csv
f = open('German.csv','r')
data = list();
for line in csv.reader(f):
    data.append(line)
f.close()


recipe = list()
food = list()
str_food = ""
for i in range(0,len(data)-1):
    if ( i == len(data)-2):
        str_food += "\""+data[i][1]+"\"" + "," + "\""+data[i+1][1]+"\""
        food.append(str_food)
        recipe.append(data[i+1][0])
    elif(data[i][0] == data[i+1][0]):
        str_food += "\""+data[i][1]+"\"" +","
    elif(data[i][0] != data[i+1][0]):
        str_food += "\""+data[i][1]+"\""
        food.append(str_food)
        recipe.append(data[i][0])
        str_food = ""

try:
    if len(recipe) == len(food) :
        print("The number of recipe and food are equal")
except:
    print("The number of recipe and food are not equal")


str_csv=""
idf_csv=""

for i in range(0,len(recipe)):
    str_csv += "\""+recipe[i]+"\"" + "," + food[i] + "\n"
    
for i in range(0,len(food)):
    idf_csv += food[i] + ","

idf_csv = idf_csv.replace(",","\n")

fp = open("German_re.csv","w")
fp.write(str_csv)
fp.close()

fp = open("German_idf.csv","w")
fp.write(idf_csv)
fp.close()

