#Enable open source modules to enable certain libraries and excuse any restrictions
import pandas as pd

from matplotlib import pyplot as Ploter

import numpy as npack

#Import the data that is saved under the created folder
data = pd.read_csv('tips.csv', index_col=0)


#Create a new column that has a calculation
data["discount"] = data["tip"]/data["size"] 


#Refine the data by creating a subset based on conditions for females
cb = data[data.time == "Dinner"]
cb2 = cb[cb.smoker == "Yes"]
cb3 = cb2[cb2.sex == "Female"]

#Create a subset based on the conditions made for males
ca2 = cb[cb.smoker == "Yes" ]
ca3 = ca2[ca2.sex == "Male"]
#print(ca3)

#Create Coefficiency between tip and total bill
datam = pd.read_csv('tips.csv')
correlation = datam['tip'].corr(datam['total_bill'])

#Create a graph for gender and discount
Ploter.plot(ca3.sex, ca3.discount)
Ploter.plot(cb3.sex, cb3.discount)
#Create Title
Ploter.title('Gender Tipping Rates', color= 'yellow', fontsize = 'x-large')
#Create Legend
Ploter.legend(['Males','Females'], fontsize = 'large')
#Create the axis labels
Ploter.xlabel('Gender', fontsize = 'x-large')
Ploter.ylabel('Tip rate per number of customers on a table', fontsize = 'x-large')
#Show the graph
Ploter.show()







