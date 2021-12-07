import csv
with open('class2.csv',newline='')as f:
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


df=pd.read_csv('class2.csv')
fig=px.scatter(df,x='Student Number',y='Marks')
fig.show()

