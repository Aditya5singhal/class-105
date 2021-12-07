import csv
import pandas as pd
import plotly.express as px


with open('class1.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
total_marks = 0
total_entries = len(filedata)

for marks in filedata:
    total_marks += float(marks[1])

mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))



     


import pandas as pd
import plotly.express as px

df=pd.read_csv('class1.csv')
fig=px.scatter(df,x='Student Number',y='Marks')
fig.show()


import math
squarelist=[]
for i in filedata:
    a=int(i)-mean(filedata)
    a=a**2
    squarelist.append(a)
    sum=0
    for i in squarelist:
        sum=sum+i

result=sum/n   
sd=math.sqrt(result) 
print(sd)