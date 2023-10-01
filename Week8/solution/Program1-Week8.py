# Program : 1 
# ===========================================================================================
# Create CSV File for Product Selling for 6 Months and add at-least 5 Records for 5 different products. 
# (Prod_Name, Jan ,Feb, Mar, Apr , May, Jun ) 
import csv
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
header=['Prod_Name' , 'Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun']
rows=[]
print("Enter product information:\n")
for i in range(5):
    print("Product -{}".format(i+1))
    prod_name=input("Product name:")
    print("Sells Information(In Months):")
    jan=int(input("January: "))
    feb=int(input("February: "))
    march=int(input("March: "))
    april=int(input("April: "))
    may=int(input("May: "))
    june=int(input("June: "))
    Prod_info=[prod_name,jan,feb,march,april,may,june]
    rows.append(Prod_info)
with open("D:\pythonnote\product.csv",'w',newline='') as write_file:
    records=csv.writer(write_file)
    records.writerow(header)
    records.writerows(rows)
# A. Read data in Dataframe. 
df=pd.read_csv("D:\pythonnote\product.csv",header=0)
# B. Add columns and calculate total_sell, average_sell. 
df['total_sell']=df['Jan']+df['Feb']+df['Mar']+df['Apr']+df['May']+df['Jun']
df['average_sell']=df['total_sell']/6
df
# C. Plot Total sell and average sell together on line chart with proper Legends, titles and lables. 
df.plot(x='Prod_Name',
        y=['total_sell','average_sell'],
        color=['red','green'])
plt.xticks(rotation = 30)
plt.xlabel('Product Names',labelpad=30)
plt.ylabel('Sells(IN INR)',labelpad=20)
plt.legend(['Total Sells','Average Sells'])
plt.title('Line Graph for Average and Total Sells')
plt.show()
# D. Explain final dataframe to csv named sell_analysis.csv 
df.to_csv("D:\pythonnote\sell_analysis.csv")
