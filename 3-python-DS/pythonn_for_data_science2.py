# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:43:06 2026

@author: Admin
"""

#31 july 2026 friday

#creating dataframe using nestedlist
import pandas as pd
technologies = [["sparks",20000, "30days"],
                ["pandas",20000, "40days"]
    
               ]
df=pd.DataFrame(technologies)
print(df)

#Since we have not given labels to columns and
#indexes, DataFrame by default assigns
#incremental sequence numbers as labels
#to both rows and columns, these are called Index.
#add column and row labels to the dataframe
column_names=["courses","fee","duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
##
df.dtypes

#You can a so assign custom
#data types to columns.
# set custom types to DataFrame
import pandas as pd
technologies = {
    'courses':["sparks","pysparks","hadoop","python","pandas","oracle","java"],
    'fee':[20000,35541,76542,87364,76576,57698,13456],
    'duration':['30days','40days','35days','40days','60days','50days','55days'],
    'discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

#convert all column
# to same datatype
df2=df.convert_dtypes()
print(df2.dtypes)

#change all columns to same type
df = df.astype(str)
print(df.dtypes)

#changes type for one to multiple column
df = df.astype({"fee": int, "discount": float})
print(df.dtypes)

#convert datatype for all columns in a list
df = pd.DataFrame(technologies)
df.dtypes
cols = ['fee', 'discount']
df[cols] = df[cols].astype('float')
df.dtypes

df = df.astype({"Courses": int})


#ignores errors
df = df.astype({"courses": int},errors='ignores')
df.dtypes

#generate error
df = df.astype({"courses": int},errors='raise')

#converts feed column to numeric type -float type
df = df.astype(str)
print(df.dtypes)
df['discount'] = pd.to_numeric(df['discount'])
df.dtypes

####
import pandas as pd
#create dataframe from dictionary
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }
df = pd.DataFrame(technologies)
df


#convert dataframe to csv
df.to_csv('data_file.csv')

#create dataframe from csv file
df = pd.read_csv('data_file.csv')

#######Pandas DataFrame
#Basic Operations
# Create DataFrame with None/NuII to work with examples

import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)


####dataframe properties
df.shape
#(8,4)
df.size
#32
df.columns
df.columns. values
df.index
df.dtypes
df.info

#accessing one column contents
df['Fee']
#accesssing two column contents
cols=['Fee','Duration']
df[cols]
df[['Fee', 'Duration']]
#select certain rows and assign it to another dataframe
df2=df[6:]
df2=df[:6]
df2


#4 august 2026 tuesday
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)


#assign new header by setting new column name
df.columns=['a','b','c','d']
df

#rename column names using rename() method
df = pd.DataFrame(technologies, index=row_labels)
df.columns=['a','b','c','d']
df2 = df.rename({'a': 'c1', 'b': 'c2'},axis=1)
df2 = df.rename({'c': 'c3', 'd': 'c4'},axis='columns')
df2 = df.rename(columns={'a': 'c1', 'b': 'c2'})


#drop dataframe rows and columns
df = pd.DataFrame(technologies, index=row_labels)

#drop rows by labels
df1 = df.drop(['r1','r2'])
df1

#delete  rows by position and index
df1 = df.drop(df.index[1])
df1
lst=[1,3]
df1=df.drop(df.index[[1,3]])
df1

#delete rows by index range
df1 = df.drop(df.index[2:])
df1

#when you have default indexex for rows
df = df = pd.DataFrame(technologies)
df1 = df.drop(0)
df1
df = pd.DataFrame(technologies)
df1 = df.drop([0,3],axis=0)
df1
df1 = df.drop(range(0,2))
df1


#dropping of columns

import pandas as pd
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df = pd.DataFrame(technologies)
print(df)

#drop column by name
#drop fee column
df2=df.drop(["Fee"],axis=1)
print(df2)

#explicitly using parameter name labels

df2=df.drop(labels=["Fee"],axis=1)

#alternatively you can also use columns instead of labels.
df2=df.drop(columns=["Fee"])


###drop column by index
df2 = df.drop(df.columns[1], axis = 1)
df = pd.DataFrame(technologies)

#using inplace=true
df.drop(df.columns[2], axis = 1, inplace=True)
print(df)

############
df = pd.DataFrame(technologies)
df2 = df.drop(df.columns[[0,1]], axis = 1)
print(df2)


#############pandas select rows by index (position/labels) use by iloc
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",
               None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days',
                '35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies, index=row_labels)
print(df)

#df.iloc[startrow:endrow, startcolumn:endcolumn]

#below are quick example of columns
df2 = df.iloc[:, 0:2]
df2

#This line uses the slicing operator to get DataFrame
# items by index.
# The first slice [ : ] indicates to return all rows.
#The second slice specifies that only columns
#tbetween 0 and 2 (excluding 2) should be return .

df2 = df.iloc[0:2, :] 
df2
#In this case, the first slice [0: 2] is
#requesting only rows O through lof the DataFrame.
#The second slice [ : ] indicates that all columns are required.
#Slicing Specific Rows and Columns using i loc attribute

df3 = df.iloc[1:2, 1:3] 
df3


#another example
df3 = df.iloc[:, 1:3] 
df3

#The second operator [1: 3] yields columns 1 and 3 only.
# Select Rows by Integer Index

df2 = df.iloc[2] 
df2 = df.iloc[[2]]  #select row by index
df2



df2 = df.iloc[[2,3,6]]  #select row by index list
df2 = df.iloc[1:5]     #select row by integer index range
df2 = df.iloc[:1]       #select first rows
df2 = df.iloc[:3]      #select first 3 rows
df2 = df.iloc[-1:]     #select last row
df2 = df.iloc[-3:]     #select last 3 rows
df2 = df.iloc[::2]      #select alternate rows 

#select rows by index
df2 = df.loc['r2']
df2 = df.loc[['r2']] #select rows by labels
df2
df2 = df.loc[['r2','r3','r6']]  #select rows by index label list
df2 = df.loc['r1':'r5']

#this will not work like 1:5 , it is using labels
#select rows by labels df2


#select columns between two columns
df2 = df.loc[:,'Fee':'Discount']
#select columns by range
df2 = df.loc[:,'Duration':]

#select columns by range
#all the columns upto duration
df2 = df.loc[:,:'Duration']


#Pandas.DataFrame. query() by Examples
# Query all rows with Courses equals • Spark •
df2=df.query("Courses == 'Spark'")
print(df2)

#not equal to condition
df2=df.query("Courses != 'Spark'")
print(df2)


#5 august 2026 wednesday


#pandas adding column to dataframe


import pandas as pd
import numpy as np
technologies   = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,25000],
    'Discount':[0.1,0.2,0,0.5,0.1]
          }
df = pd.DataFrame(technologies)
print(df)


#pandas add column to dataframe
#add new column to dataframe
tutors = ['ram', 'sham', 'ganesh', 'ramesh', 'ashish']
df2 = df.assign(tutorsassigned=tutors)
print(df2)

#add multiple column to the dataframe

mnccompanies = ['tata', 'hcl', 'tcs', 'wipro', 'capgemini']
df2 = df.assign(mnc=mnccompanies,tutors=tutors)
df2

#derive new column from existing column

df = pd.DataFrame(technologies)
df2 = df.assign(discount_percent=lambda x: x.Fee * x.Discount / 100)
print(df2)

##append column to existing pandas dataframe
#add new column to the existing dataframe


df = pd.DataFrame(technologies)
df["mnccompanies"] = mnccompanies
print(df)

#add new column at the specific position
df = pd.DataFrame(technologies)
df.insert(0, 'tutors', tutors)
print(df)

##Quick Examples  of Get the Number of Rows in DataFrame

rows_count = len(df.index)
rows_count 
rows_count = len(df.axes[0])
rows_count 
column_count = len(df.axes[1])
column_count 


#
df = pd.DataFrame(technologies)
df.shape
rows_count = df.shape[0] #return number of rows
rows_count
col_count = df.shape[1] #return number of columns
col_count

#pandas Apply Function to a Column
#Below are quick examples
#Using Dataframe.apply() to apply function add colum
import pandas as pd
import numpy as np

data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
       }

df = pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2 = df.apply(add_3)
df2 
df2=((df.A).apply(add_3))

#apply function on multiple columns


import pandas as pd
import numpy as np

data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
       }

df = pd.DataFrame(data)
print(df)

def add_4(x):
    return x+4
df["B"] = df["B"].apply(add_4)
df["B"]

df = pd.DataFrame(data)
##apply function on multiple columns

df[['A', 'B']] = df[['A', 'B']].apply(add_4)
df
df = pd.DataFrame(data) 
##apply lambda function on each column
df2 = df.apply(lambda x : x+4)
df2

#using pandas.dataframe.transform()
#using tranform function to apply function
df = pd.DataFrame(data) 
def add_2(x):
    return x+2
df = df.transform(add_2)
print(df)

#using map function
df = pd.DataFrame(data) 
df
df['A'] = df['A'].map(lambda A: A/2.)
print(df)

#using numpy function
import numpy as np

df = pd.DataFrame(data) 
df
df['A'] = df['A'].apply(np.square)
print(df)

#using numpy.square()method
#using numpy.square() and [] operator
df = pd.DataFrame(data) 
df
df['A'] = np.square(df['A'])
print(df)

#Pandas groupby()  With Examples 
import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
print(df)

#use groupby() to compute the sum
df2 = df.groupby(['Courses']).sum()
print(df2)

#group by multiple column
df = pd.DataFrame(technologies)
df2 = df.groupby(['Courses', 'Duration']).sum()
print(df2)



#pandas shuffle dataframe rows


import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day','40days','35days','40days','60days','50days','55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
df = pd.DataFrame(technologies)
print(df)

#Pandas Shuffle DataFrame Rows
# shuffle the DataFrame rows & return all rows

df1 = df.sample(frac = 1)
print(df1)
df1 = df.sample(frac = 0.5)
print(df1)

#create a new index starting from zero
df1 = df.sample(frac = 1).reset_index()
print(df1)

#drop shuffle index
df1 = df.sample(frac = 1).reset_index(drop=True)
print(df1)


#joins
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)


#pandas inner join is mostly used join,
#1t is used to join two DataFrames on indexes.
#When indexes don't match the rows get dropped from both DataFrames.
# pandas Inner join DataFrames

df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')
print(df3)

#pandas join, by default it will be join the table left join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right")
print(df3)
#pandas left join in dataframe
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how='left')
print(df3)

#pandas right join in dataframe
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')
print(df3)





#6 august 2026 thursday

#What is NumPy?
#The NumPy library is a popular open-source Python
#1 ibrary used for scientific computing applications,
# and it stands for Numerical Python,
#which is consisting of multidimensional array
#objects and a collection Of routines for processing those arrays.
#lnstall Python NumPy Library
#goto base terminal and on prompt
#pip install numpy
# Install NumPy using Conda
#conda install numpy

#arrays in numpy
#create ndarray
import numpy as np
arr = np.array([10,20,30])
print (arr)

#create multidimensional array
arr = np.array([[10,20,30],[40,50,60]])
print (arr)

#Represent The Minimum Dimensions
#Use ndmin param to specify how many minimum
#dimensions you wanted to create an array with
# Minimum dimension
arr = np.array([10,20,30,40], ndmin=3)
print (arr)

#change the datatype
#dtype parameter
arr = np.array([10,20,30], dtype = complex)
print (arr)

#Get The Dimensions of an Array
# Get dimension of an array

arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print (arr)
print (arr. ndim)


# Finding the size of each item in the array
arr = np.array([10,20,30])
print("each item contain in bytes :",arr.itemsize)



#Get The Data Type of Each Array Item
# Finding the data type of each array item


arr = np.array([10,20,30])
print("each item is of the type :",arr.dtype)

#Get the Shape and Size of Array

arr = np.array([[10,20,30],[40,50,60]])
print (arr)
print("array size:", arr.size)
print("shape:", arr.shape)

# Creating array from list with type float

arr = np.array([[10,20,30],[40,50,60]], dtype = float)
print( "Array created by using list: \n", arr)

#Create a Sequence of Integers using arange()
# Create a sequence of integers
#from 0 to 20 with steps of 3
arr = np.arange(0, 20, 3)
print( "A sequential array with steps of 3 : \n", arr)


# A sequential array with steps 0 3:
# [ 0 3 6 912 15 18]
# Access single element using index
arr = np.arange(11)
print (arr)
print (arr[2])
print (arr[-2])

#Mu1ti-Dimenstiona1 Array Indexing
# Access multi-dimensional array element
# using array indexing
arr = np.array([[10,20,30,40,50],[20,30,50,10,30]])
print (arr)

print(arr.shape)

print(arr[1,1])
print(arr[0,4])
print(arr[1,-1])


#Access array elements using slicing
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)
x= arr[1:8:2]
print(x)

# example
x= arr[-2:3:-1]
print(x)

x= arr[-2:10]
print(x)

x= arr[8:0:-1]
print(x)


#Slicing array
#For multi-dimensional NumPy arrays,

import numpy as np
# indexing in numpy
multi_arr = np.array([[10,20,30,40],
                      [40,50,70,90],
                      [60,10,70,80],
                      [30,90,40,30]])
print(multi_arr)

#you can access the elements as below
print(multi_arr[1,2])#TO access the value at row I and column 2.

print(multi_arr[1,:]) #To get the value at row 1 and al columns.

print(multi_arr[:,1])#- Access the value at all rows and columns 1.

x=multi_arr[:3, ::2]
print(x)

#lnteger Array Indexing
#lnteger array indexing allows the selection of arbitrary items

import numpy as np
# Integer array indexing
arr = np.arange(35).reshape(5,7)
print(arr)


#boolean array indexing


import numpy as np
# boolean array indexing
arr = np.arange(12).reshape(3,4)
print(arr)

rows = np.array([False,True,True])
rows
wanted_rows=arr[rows, :]
print(wanted_rows)


#create array
array = np.array([10,20,30,40])
print("array:", array)
print(type(array))
#convert to list
lst = array.tolist()
print("list:", lst)
print(type(lst))


# Convert Multi Dimensional Array to list
# create array
array = np.array([[10,20,30,40],
                      [40,50,70,90],
                      [60,10,70,80],
                      ])
print("array:", array)

#convert list
lst = array.tolist()
print("list:", lst)

#numpy . asarray()
#Using numpy.asarray()
#This function calls the numpy.array() function
#inside itself.
list = [20,30,40,50]
array = np.asarray(list)
print("array:", array)
print(type(array))

#ndarray.shape

#shape
array = np.array([[1,2,3],[4,5,6]])
array
print(array.shape)
print(array.ndim)
print(array.itemsize)
print(array.size)
print(array.dtype)



#7 august 2026 friday

#matrix
import numpy as np
# 1. Square Matrix (same number of rows and columns)
square_matrix = np.array([[1,2],[3,4]])
print("1.square matrix:\n", square_matrix)

# 2. Rectangular Matrix (rows columns)
rect_matrix = np.array([[1,2,3],[4,5,6]])
print("\n2. rectangular matrix:\n", rect_matrix)

# 3. Diagonal Matrix (non-zero elements only on main diagonal)
diagonal_matrix = np.diag([10,20,30])
print("\n3. matrix:\n", diagonal_matrix)

#4. Scalar Matrix (diagonal matrix with equal diagonal elements)

scalar_matrix = np.diag([5,5,5])
print("\n4. scalar matrix:\n", scalar_matrix)

# 5. Identity Matrix (Is on diagonal, 0s elsewhere)
identity_matrix = np.eye(3)
print("\n5. identity matrix:\n", identity_matrix)


# 6. Zero Matrix (all elements are 0)
zero_matrix = np.zeros((3,3))
print("\n6. zero matrix:\n", zero_matrix)



# 7. Ones Matrix (all elements are I)
ones_matrix = np.ones(3)
print("\n7. ones matrix:\n", ones_matrix)

#8. Upper Triangular Matrix (zeroes below diagonal)

upper_triangular = np.array([[1,2,3],
                            [0,4,5],
                            [0,0,6]])
print("\n8. upper triangular:\n", upper_triangular)

#9. lower Triangular Matrix (zeroes below diagonal)

lower_triangular = np.array([[1,0,0],
                            [2,3,0],
                            [4,5,6]])
print("\n8. lower triangular:\n", lower_triangular)


# 10. Symmetric Matrix (matrix transpose)
symmetric_triangular = np.array([[1,7,3],
                            [7,4,-5],
                            [3,-5,6]])
print("\n10. symmetric triangular:\n", symmetric_triangular)

# 11. Skew-Symmetric Matrix (matrix == -transpose)

skew_symmetric = np.array([[0,2,-1],
                            [-2,0,-4],
                            [1,4,0]])
print("\n11. skew-symmetric:\n", skew_symmetric)
# 12. Sparse Matrix (many zero entries)

sparse_matrix = np.array([[0,0,0],
                            [0,9,0],
                            [0,0,0]])
print("\n8. Sparse Matrix:\n", sparse_matrix)

# 13.Row Matrix 1 row,n columns

row_matrix = np.array([[1,2,3]])
print("\n13. row matrix:\n", row_matrix )

# 14. Column Matrix (n rows, 1 column)
column_matrix = np.array([[1],
                          [2],
                          [3]])
print("\n14. column matrix:\n", column_matrix )


# 15. Singleton Matrix (IXI matrix)

singleton_matrix = np.array([[42]])
print("\n15. singleton matrix:\n", singleton_matrix )

#matrix operation


#addition
a = np.array([[1,2],[3,4]])
print(a)
b = np.array([[5,6],[7,8]])
print(b)
addition = a+b
print( "\nMatrix Addition: \n",addition)


#subtraction
subtraction = a-b
print( "\nMatrix Subtraction: \n",subtraction)


#scalar multiplication

scalar_mult = 2 * a
print( "\nscalar multiplication: \n",scalar_mult)

#matrix multiplication(dot product)

matrix_mult = np.dot(a, b)
print( "\nmatrix multiplication (dot product): \n",matrix_mult)

# 12. Transpose
transpose_a = a.T

print("\nTranspose of a:\n", transpose_a)

#13 Determinant
det_a = np.linalg.det(a)
print( "\ndeterminant of a: \n",det_a)


#14 inverse
if np.linalg.det(a) != 0:
    inverse_a = np.linalg.inv(a)
    print("\ninverse of a:\n", inverse_a)
else:
    print("\nmatrix a is singular (no inverse).")




# 16. Trace
#The trace of a square matrix is the sum of its diagonal elements.
#0n1y defined for square matrices.
#Used in linear algebra, quantum mechanics, and machine learning.
#Re1ated to the sum of eigenvalues of the matrix.

a
trace_a = np.trace(a)
print("\ntrace of a:\n", trace_a)

# 17. Eigenvalues and Eigenvectors
eig_vals, eig_vecs = np.linalg.eig(a)
print("\neigenvalues of a:\n", eig_vals)
print("eigenvectors of a:\n", eig_vecs)



#Use Case l: Student Marks Analysis
#Scenario
#A teacher wants to analyze the marks of students in five subjects.
# Import NumPy library

import numpy as np

# Store marks of five students
marks = np.array([78, 85, 92, 66, 81])
# Display marks

print( "Student Marks =", marks)
# Calculate average marks
print( "Average Marks =", np.mean(marks))
# Find highest marks

print( "Highest Marks =", np.max(marks))
# Find lowest marks

print( "Lowest Marks =", np.min(marks))
# Find total marks

print( "Total Marks =", np.sum(marks))





#Use Case 2: Employee Salary Analysis
#Scenario
#An HR department wants to increase every employee's salary by 10%.
import numpy as np
#employee salaries
salary = np.array([25000, 32000, 28000, 45000, 38000])
print("current salary")
print(salary)
#increase salary by 10%
new_salary = salary * 1.10
print("\nsalary after 10% increment")
print(new_salary)
#average salary
print("\naverage salary =", np.mean(new_salary))


####
import numpy as np
# 3x3 grayscale image (pixel values: 0-255)
image = np.array([[50, 80, 120],
                 [60, 100, 140],
                 [70, 110, 150]])


print( "Original Image")
print(image)

# Increase brightness by 30
bright_image = image + 30


# Pixel values cannot exceed 255
bright_image = np.clip(bright_image, 0, 255)

print( "\nBrightened Image")
print(bright_image)


###
import numpy as np
#1 = Spam word found
# 0 = Normal word
spam_words = np.array([1,0,1,1,0,0,1,0,1])

print( "Spam Indicators ")

print(spam_words)

print("\nTotal Spam Words =", np.sum(spam_words))

if np.sum(spam_words) >=4:
    print("prediction : Spam Email")
else:
    print("prediction : Normal Email")












































































