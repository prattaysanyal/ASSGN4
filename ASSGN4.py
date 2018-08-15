#Q.1 - Create a dataframe with your name , age , mail id and phone number and
add your friends’s information to the same.

import pandas as pd
import numpy as np
context = {
    'Name':['Prattay','Ankita','Shubham'],
    'Age' :[21,23,21],
    'Email_id':['prattay0022@gmail.com','anki@gmail.com','sid@gmail.com'],
    'Phone_no' :[8527948511,8368750600,8588033135]
     }
print("Your Dataframe is as follows: ")
df = pd.DataFrame(context)
df

#Q.2 - Download the dataset from this link , 

#Import the data and print the following :
#a.) First 5 rows of Dataframe 
#b.) First 10 rows of the Dataframe 
#c.) find basic statistics on the particular dataset. 
#d.) Find the last 5 rows of the dataframe 
#e.) Extract the 2nd column and find basic statistics on it.


file = pd.read_csv("weather.csv")
print("data frame is")
file
print("The first five rows of the dataframe are:")
file.head()
print("The first ten rows of the dataframe are:")
file.head(10)
print("Basic statistics of the dataframe are:")
file.describe(include='all')
print("The last five rows of the dataframe are:")
file.tail()
print("Basic statistics of 2nd column is:")
file.describe(include='all').Location
