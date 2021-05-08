'''
This program converts a csv file to a list and gets the standard deviation
'''
import csv
import pandas as pd
import math
import statistics

# opening the file as a list 

f = open('data.csv') 
reader = csv.reader(f)
# file1 = list(reader)
for row in reader:
    file1 = row

#converting the string values of the list into float

file_1 = []
for item in file1:
    file_1.append(float(item))

#getting the mean using the mean function of the statistics module  
m1=statistics.mean(file_1)
   
squared_list1 = []
#carrying out the standard deviation formula
for i in file_1:
  a = i - m1
  a = a**2
  squared_list1.append(a)

sum = 0
for i in squared_list1:
  sum = sum+i
result = sum/( len(squared_list1) - 1) 
sd = math.sqrt(result)
 
#printing the standard deviation in 2 decimal points 
print('The standard deviation is: ',float("{:.2f}".format(sd))) 