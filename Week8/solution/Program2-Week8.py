# Program : 2 
# ==================================================================================================
# Sales (sid, year, totalsales)
# Create above table into a SQLite database with appropriate constraints.
import sqlite3 as sq
import pandas as pd
import csv
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
conn=sq.connect('D:\database\sales.db')
cur=conn.cursor()
cur.execute('CREATE TABLE Sales(sid text PRIMARY KEY, year int, totalsales int)')
conn.commit()
# A. Insert at least 5-10 records into the sales table
L=[]
print('Enter 10 Records:-\n')
for i in range(10):
    print('Record {}-'.format(i+1))
    sid=input("Sales ID: ")
    year=int(input("Year: "))
    totalsales=int(input("Total Sales: "))
    t=(sid,year,totalsales)
    L.append(t)
cur.executemany('INSERT INTO Sales VALUES(?,?,?);',L)
# B. Export sales table data into sales.csv file.
cur.execute('SELECT * FROM Sales')
data=cur.fetchall()
conn.close()
header=['Sid','Year','Total Sales']
with open('D:\pythonnote\sales.csv','w',newline='') as write_obj:
    writer=csv.writer(write_obj)
    writer.writerow(header)
    writer.writerows(data)
# C. Write a python scripts that read the sales.csv file and plot a bar chart that shows totalsales of the year. 
df=pd.read_csv('D:\pythonnote\sales.csv',header=0)
df.plot(kind='bar',
        x='Year',
        y='Total Sales',
        color=['red','cyan','yellow','green','pink','orange','blue','grey','violet','indigo'])
plt.yticks([10000,20000,30000,40000,50000,60000])
plt.xticks(rotation=30)
plt.xlabel('Years',labelpad=30)
plt.ylabel('Sales',labelpad=20)
plt.legend(['Sales'])
plt.title('Total Sales per Year')
plt.show()
