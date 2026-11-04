# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:24:34 2026

@author: Admin
"""

#profile test 5 , 03 august 2026, monday
'''       
  
Q1. Without using any built-in functions like min(), write a Python program to: 
1. Define a list manually with some integers, e.g., arr = [3, 7, 2, 9, 5]. 
2. Find the minimum value in the list using a for loop and conditional statements. 
3. Create a new list by adding the minimum value to each element of the original list. 
4. Create another list by multiplying each element of the original list by the minimum 
value. 
 Print:The original list ,The minimum value,The list after addition,The list after 
multiplication, Constraints:Do not use any built-in functions like min(), map(), sum(), 
etc.Use only loops and basic operations. '''

# Define the list manually
arr = [3, 7, 2, 9, 5]

# Find the minimum value without using min()
minimum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num

# Create a new list by adding the minimum value to each element
addition_list = []

for num in arr:
    addition_list.append(num + minimum)

# Create another list by multiplying each element by the minimum value
multiplication_list = []

for num in arr:
    multiplication_list.append(num * minimum)

# Print the results
print("Original List:", arr)
print("Minimum Value:", minimum)
print("List after Addition:", addition_list)
print("List after Multiplication:", multiplication_list)






'''
Q2. Given the list , lst = [10, 20, 4, 45, 99, 99] ,find the second smallest number. '''


# Given list
lst = [10, 20, 4, 45, 99, 99]

# Initialize smallest and second smallest
smallest = float('inf')
second_smallest = float('inf')

# Find the smallest and second smallest numbers
for num in lst:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

# Print the result
print("List:", lst)
print("Second Smallest Number:", second_smallest)





''' 
Q.3 Write a Python function read_file_safely(filename) that: 
Handles: 
 FileNotFoundError — if the file does not exist, print: 
Error: The file <filename> was not found. 
PermissionError — if the program does not have permission to read the file, print: 
Error: Permission denied for file <filename>. 
If no error occurs, prints: 
File read successfully '''


def read_file_safely(age):
    try:
        file = open(age, "r")
        file.read()
        print("File read successfully")
        file.close()

    except FileNotFoundError:
        print(f"Error: The file {age} was not found.")

    except PermissionError:
        print(f"Error: Permission denied for file {age}.")


# Example usage
filename = input("Enter the file name: ")
read_file_safely(age)







'''
Q.4     Write a Python program that: 
 Reads a text file named article.txt 
 Counts the frequency of each word (ignore case and punctuation) 
 Stores the results in a new file called word_count.txt in the format: '''







'''
Q.5   Write a program that accepts student marks as input. 
 Raise a ValueError if marks are negative or greater than 100 
 Handle the exception and print "Invalid Marks" 
 Otherwise, print grade based on marks 
'''

try:
    # Accept marks as input
    marks = int(input("Enter student marks: "))

    # Check for invalid marks
    if marks < 0 or marks > 100:
        raise ValueError("Invalid Marks")

    # Display grade
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

except ValueError:
    print("Invalid Marks")

#profile test 6 , 10 august 2026, monday

'''Question 1: Student Marks Analysis using Pandas Series
Scenario:
A college wants to maintain the marks obtained by four students in a Data Science test. The faculty wants to use a Pandas Series where the student names are used as index labels.
Task: Write a Python program using Pandas Series to:
1.	Create a Series named marks with the following data:
o	Rahul – 78
o	Priya – 85
o	Amit – 67
o	Sneha – 92
2.	Display the complete Series and its index.
3.	Display the marks obtained by Priya using the appropriate Series indexing technique.
4.	Update Rahul's marks from 78 to 82.
5.	Calculate and display the average marks of all students.
6.	Add the following students to the existing Series using pd.concat():
o	Neha – 88
o	Raj – 73
7.	Display the final Series.
Concepts tested:
Series creation, index, .loc[], updating values, .mean(), and pd.concat().
________________________________________'''

import pandas as pd

# 1. Create a Series named marks
marks = pd.Series(
    [78, 85, 67, 92],
    index=["Rahul", "Priya", "Amit", "Sneha"]
)

# 2. Display the complete Series and its index
print("Complete Series:")
print(marks)

print("\nIndex of the Series:")
print(marks.index)

# 3. Display the marks obtained by Priya using .loc[]
print("\nMarks obtained by Priya:")
print(marks.loc["Priya"])

# 4. Update Rahul's marks from 78 to 82
marks.loc["Rahul"] = 82

print("\nSeries after updating Rahul's marks:")
print(marks)

# 5. Calculate and display the average marks
average_marks = marks.mean()

print("\nAverage marks of all students:")
print(average_marks)

# 6. Add new students using pd.concat()
new_students = pd.Series(
    [88, 73],
    index=["Neha", "Raj"]
)

marks = pd.concat([marks, new_students])

# 7. Display the final Series
print("\nFinal Series:")
print(marks)


'''Question 2: Employee Attendance Analysis with Missing Data
Scenario:
An organization records the number of days attended by four employees during a particular month. Due to a data-entry problem, the attendance of one employee is missing.
The data is:
Employee	Days Present
Amit	22
Priya	24
Rahul	NaN
Sneha	21
Task: Write a Python program using Pandas Series to:
1.	Create a Series named attendance using the employee names as the index.
2.	Display the Series and its data type.
3.	Calculate the average attendance, ignoring the missing value.
4.	Replace the missing value (NaN) with 23 using fillna().
5.	Display the updated Series.
6.	Remove the employee whose attendance is missing before filling the missing value, using dropna().
(Create the Series again if required.)
7.	Convert the final attendance values into integers.
Concepts tested:
Series creation, named index, NaN, mean(), fillna(), dropna(), and data-type conversion.
Certainly. Let us use a completely different real-world use case while testing the same Pandas 
DataFrame concepts.'''

import pandas as pd

# 1. Create a Series named marks
marks = pd.Series(
    [78, 85, 67, 92],
    index=["Rahul", "Priya", "Amit", "Sneha"]
)

# 2. Display the complete Series and its index
print("Complete Series:")
print(marks)

print("\nIndex of the Series:")
print(marks.index)

# 3. Display the marks obtained by Priya using .loc[]
print("\nMarks obtained by Priya:")
print(marks.loc["Priya"])

# 4. Update Rahul's marks from 78 to 82
marks.loc["Rahul"] = 82

print("\nSeries after updating Rahul's marks:")
print(marks)

# 5. Calculate and display the average marks
average_marks = marks.mean()

print("\nAverage marks of all students:")
print(average_marks)

# 6. Add new students using pd.concat()
new_students = pd.Series(
    [88, 73],
    index=["Neha", "Raj"]
)

marks = pd.concat([marks, new_students])

# 7. Display the final Series
print("\nFinal Series:")
print(marks)

'''Question 3:Use Case: Hospital Patient Record Analysis
Scenario:
A hospital maintains basic information about patients admitted to different departments. The hospital administrator wants to analyze patient records to understand treatment costs and identify patients with higher medical expenses.
The available data is:
patients = {
    'Patient': ["Amit", "Priya", "Rahul", "Sneha", "Kiran"],
    'Department': ["Cardiology", "Orthopedics", "General", "Cardiology", "Neurology"],
    'Age': [45, 32, 60, 52, 41],
    'Treatment_Cost': [85000, 45000, 25000, 95000, 70000]
}
Write a Python program using Pandas DataFrame to:
1.	Create a DataFrame using the above dictionary.
2.	Display the DataFrame, its number of rows and columns, and data types.
3.	Display only the Patient and Treatment_Cost columns.
4.	Display the details of patients whose Treatment_Cost is greater than ₹50,000.
5.	Select the first three patient records using iloc.
6.	Add a new column Insurance_Cover assuming that the insurance covers 60% of the Treatment_Cost.
7.	Calculate and display the average Treatment_Cost.
8.	Display the final DataFrame.
Concepts covered:
DataFrame creation, shape, dtypes, column selection, filtering, iloc, adding a derived column, and average calculation.
Certainly. Here is the revised single scenario-based question, with points 3 and 4 removed 
and the requested Pandas operations added.'''


import pandas as pd

patients = {
    'Patient': ["Amit", "Priya", "Rahul", "Sneha", "Kiran"],
    'Department': ["Cardiology", "Orthopedics", "General", "Cardiology", "Neurology"],
    'Age': [45, 32, 60, 52, 41],
    'Treatment_Cost': [85000, 45000, 25000, 95000, 70000]
}
df = pd.DataFrame(patients)
print(df)

df = pd.DataFrame(patients)
df.shape
rows_count = df.shape[0] #return number of rows
rows_count
col_count = df.shape[1] #return number of columns
col_count

import pandas as pd

# 1. Create a DataFrame using the given dictionary
patients = {
    'Patient': ["Amit", "Priya", "Rahul", "Sneha", "Kiran"],
    'Department': ["Cardiology", "Orthopedics", "General", "Cardiology", "Neurology"],
    'Age': [45, 32, 60, 52, 41],
    'Treatment_Cost': [85000, 45000, 25000, 95000, 70000]
}

df = pd.DataFrame(patients)

# 2. Display the DataFrame, number of rows and columns, and data types
print("Patient DataFrame:")
print(df)

print("\nNumber of Rows and Columns:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# 3. Display only Patient and Treatment_Cost columns
print("\nPatient and Treatment Cost:")
print(df[['Patient', 'Treatment_Cost']])

# 4. Display patients whose Treatment_Cost is greater than ₹50,000
print("\nPatients with Treatment Cost greater than ₹50,000:")
print(df[df['Treatment_Cost'] > 50000])

# 5. Select the first three patient records using iloc
print("\nFirst Three Patient Records:")
print(df.iloc[:3])

# 6. Add Insurance_Cover column (60% of Treatment_Cost)
df['Insurance_Cover'] = df['Treatment_Cost'] * 0.60

print("\nDataFrame after adding Insurance Cover:")
print(df)

# 7. Calculate and display average Treatment_Cost
average_cost = df['Treatment_Cost'].mean()

print("\nAverage Treatment Cost:")
print(average_cost)

# 8. Display the final DataFrame
print("\nFinal DataFrame:")
print(df)


'''Question 4:Use Case: Employee Salary Hike and Churn Analysis
Scenario:
An organization wants to analyze employee salary hikes and churn-out rates to identify employees 
who may be at higher risk of leaving the organization. The HR department has provided the data in
 emp_data.csv.
Write a Python program using Pandas to perform the following operations on the given emp_data.csv 
dataset:
1.	Read the dataset using pd.read_csv() and display the complete DataFrame.
2.	Display the following basic information about the dataset:
o	Number of rows and columns using shape
o	Column names using columns
o	Data types using dtypes
3.	Select columns to display only Salary_hike and Churn_out_rate.
4.	Slice the DataFrame using iloc to display the first 5 rows and first 2 columns.
5.	Slice the DataFrame using loc to display the required rows and columns using their labels.
6.	Display records where Churn_out_rate is greater than 50.
7.	Add multiple new columns:
o	Hike_Category
o	Risk_Level
8.	Derive a new column Expected_Churn from the existing Churn_out_rate column using the 
following formula:
Expected_Churn = Churn_out_rate × 1.10
9.	Use the apply() function to create the Risk_Level column:
o	If Churn_out_rate > 50 → "High Risk"
o	Otherwise → "Low Risk"
10.	Use the apply() function with a lambda function to create Hike_Category:
•	If Salary_hike >= 1700 → "High Hike"
•	Otherwise → "Low Hike"
11.	Display the final DataFrame with the original and newly derived columns.
Certainly. Based on the attached material, which covers NumPy arrays, indexing, slicing, 
arithmetic operations, and practical use cases such as student marks, salary, image, and 
sales analysis, here is one scenario-based question.'''




'''Question 5:Use Case: Monthly Electricity Consumption Analysis
Scenario:
A household records its electricity consumption for 6 months in units. The electricity department wants to analyze the consumption using NumPy and identify periods of high and low electricity usage.
The recorded consumption is:
[320, 280, 350, 410, 390, 450]
Write a Python program using NumPy to:
1.	Create a NumPy array to store the monthly electricity consumption.
2.	Display the array, its shape, size, and data type.
3.	Display the consumption of the third month using array indexing.
4.	Extract the consumption of the first three months using slicing.
5.	Calculate the total and average electricity consumption.
6.	Find the maximum and minimum consumption.
7.	Increase the consumption values by 10% to simulate a projected increase in future usage.
8.	Create a Boolean array to identify months where consumption is greater than 350 units 
and display those consumption values.'''

import numpy as np

# 1. Create a NumPy array to store monthly electricity consumption
consumption = np.array([320, 280, 350, 410, 390, 450])

# 2. Display the array, shape, size, and data type
print("Electricity Consumption Array:")
print(consumption)

print("\nShape of Array:")
print(consumption.shape)

print("\nSize of Array:")
print(consumption.size)

print("\nData Type:")
print(consumption.dtype)

# 3. Display the consumption of the third month using indexing
print("\nConsumption of Third Month:")
print(consumption[2])

# 4. Extract consumption of the first three months using slicing
print("\nConsumption of First Three Months:")
print(consumption[:3])

# 5. Calculate total and average electricity consumption
total = np.sum(consumption)
average = np.mean(consumption)

print("\nTotal Electricity Consumption:")
print(total)

print("\nAverage Electricity Consumption:")
print(average)

# 6. Find maximum and minimum consumption
maximum = np.max(consumption)
minimum = np.min(consumption)

print("\nMaximum Consumption:")
print(maximum)

print("\nMinimum Consumption:")
print(minimum)

# 7. Increase consumption values by 10%
projected_consumption = consumption * 1.10

print("\nProjected Consumption after 10% Increase:")
print(projected_consumption)

# 8. Create Boolean array for consumption greater than 350 units
condition = consumption > 350

print("\nBoolean Array:")
print(condition)

print("\nConsumption Greater Than 350 Units:")
print(consumption[condition])



#profile test 7 , 17 august 2026, monday


'''Question 1: Use-Case Based Question: Crime Data Analysis Using Pandas
Scenario
A government crime-analysis department wants to analyze crime patterns across different states. The department has provided the file crime_data.csv, which contains the following information:
•	State – Name of the state 
•	Murder – Murder crime rate 
•	Assault – Assault crime rate 
•	UrbanPop – Percentage of urban population 
•	Rape – Rape crime rate 
The data analyst has been asked to use Pandas to explore the dataset and identify states that may require greater attention from law-enforcement agencies.
Task
Write a Python program using Pandas to perform the following analysis.
Part A – Understanding the Dataset
1.	Read crime_data.csv into a Pandas DataFrame named crime_df. 
2.	Display the first 5 records. 
3.	Display the last 5 records. 
4.	Find: 
o	Number of rows and columns 
o	Total number of elements 
o	Column names 
o	Data types of all columns 
5.	Display basic statistical information using describe(). 
Part B – Selecting Data
6.	Display only the Murder and Assault columns. 
7.	Display the first 10 states using iloc. 
8.	Display the last 5 states using iloc. 
9.	Select the rows corresponding to the first five states using loc. 
10.	Display the Murder, Assault, and Rape columns for the first 10 states. 
Part C – Crime Investigation
11.	Identify all states where the Murder rate is greater than 10. 
12.	Identify all states where the Assault rate is greater than 250. 
13.	Identify states where: 
•	Murder rate > 10 and 
•	Assault rate > 200. 
14.	Identify states where: 
•	Urban population > 70 
•	Rape rate > 25. 
15.	Using query(), display all states where Murder > 10. 
________________________________________'''

import pandas as pd

# ============================================================
# Part A – Understanding the Dataset
# ============================================================

# 1. Read crime_data.csv into a DataFrame named crime_df
crime_df = pd.read_csv('c:/3-python-DS/crime_data.csv')

# 2. Display the first 5 records
print("1. First 5 Records:")
print(crime_df.head())

# 3. Display the last 5 records
print("\n2. Last 5 Records:")
print(crime_df.tail())

# 4. Display information about the dataset

# Number of rows and columns
print("\n3. Number of Rows and Columns:")
print(crime_df.shape)

# Total number of elements
print("\n4. Total Number of Elements:")
print(crime_df.size)

# Column names
print("\n5. Column Names:")
print(crime_df.columns)

# Data types of all columns
print("\n6. Data Types:")
print(crime_df.dtypes)

# 5. Basic statistical information
print("\n7. Statistical Summary:")
print(crime_df.describe())


# ============================================================
# Part B – Selecting Data
# ============================================================

# 6. Display only Murder and Assault columns
print("\n8. Murder and Assault Columns:")
print(crime_df[["Murder", "Assault"]])

# 7. Display the first 10 states using iloc
print("\n9. First 10 States using iloc:")
print(crime_df.iloc[:10])

# 8. Display the last 5 states using iloc
print("\n10. Last 5 States using iloc:")
print(crime_df.iloc[-5:])

# 9. Select rows corresponding to the first five states using loc
print("\n11. First 5 States using loc:")
print(crime_df.loc[:4])

# 10. Display Murder, Assault and Rape columns for first 10 states
print("\n12. Murder, Assault and Rape for First 10 States:")
print(crime_df.loc[:9, ["Murder", "Assault", "Rape"]])


# ============================================================
# Part C – Crime Investigation
# ============================================================

# 11. States where Murder rate is greater than 10
print("\n13. States where Murder rate > 10:")
print(crime_df[crime_df["Murder"] > 10])

# 12. States where Assault rate is greater than 250
print("\n14. States where Assault rate > 250:")
print(crime_df[crime_df["Assault"] > 250])

# 13. States where Murder > 10 AND Assault > 200
print("\n15. States where Murder > 10 and Assault > 200:")
print(crime_df[
    (crime_df["Murder"] > 10) &
    (crime_df["Assault"] > 200)
])

# 14. States where UrbanPop > 70 AND Rape > 25
print("\n16. States where UrbanPop > 70 and Rape > 25:")
print(crime_df[
    (crime_df["UrbanPop"] > 70) &
    (crime_df["Rape"] > 25)
])

# 15. Using query(), display states where Murder > 10
print("\n17. States where Murder > 10 using query():")
print(crime_df.query("Murder > 10"))



'''Question 2: Use-Case: Student Marks Analysis Using NumPy
A college stores marks of 3 students in Python, SQL, and Statistics using a NumPy matrix.
marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84]
])
Task: Write a NumPy program to:
1.	Display the marks of the second student. 
2.	Display the Python marks of all students. 
3.	Find the total marks of each student. 
4.	Find the average marks of each student. 
5.	Find the highest marks in each subject. 
6.	Find the transpose of the marks matrix.'''

import numpy as np

# Marks of 3 students in Python, SQL, and Statistics
marks = np.array([
    [78, 85, 90],
    [65, 72, 80],
    [88, 91, 84]
])

# 1. Display the marks of the second student
print("Marks of second student:", marks[1])

# 2. Display the Python marks of all students
print("Python marks of all students:", marks[:, 0])

# 3. Find the total marks of each student
total = np.sum(marks, axis=1)
print("Total marks of each student:", total)

# 4. Find the average marks of each student
average = np.mean(marks, axis=1)
print("Average marks of each student:", average)

# 5. Find the highest marks in each subject
highest = np.max(marks, axis=0)
print("Highest marks in each subject:", highest)

# 6. Find the transpose of the marks matrix
transpose = marks.T
print("Transpose of marks matrix:")
print(transpose)



'''Question 3: Use-Case: Penguin Species Analysis
A wildlife research team wants to analyze the physical characteristics of different penguin species using Seaborn's built-in penguins dataset.
import seaborn as sns

penguins = sns.load_dataset('penguins')
Task: Write a Python program using Seaborn to:
1.	Explore the data
Display the first 5 records, data types, and statistical summary of the dataset. 
2.	Analyze Body Measurements
Plot the distribution of body_mass_g and flipper_length_mm. Identify the general distribution and possible outliers. 
3.	Compare Penguin Species
Use a suitable categorical plot to compare the body_mass_g of different penguin species. 
4.	Study Relationships
Create a pairplot() using numerical variables and analyze the relationship between flipper_length_mm, bill_length_mm, bill_depth_mm, and body_mass_g. 
5.	Find Important Insights
Create a correlation heatmap and identify: 
o	Which two numerical features have the strongest relationship? 
o	Which penguin species generally has the highest body mass?
Please write inference of each'''


# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Seaborn's built-in penguins dataset
penguins = sns.load_dataset('penguins')

# Display first 5 records
print("\nFirst 5 Records:")
print(penguins.head())

# Display data types
print("\nData Types:")
print(penguins.dtypes)

# Display statistical summary
print("\nStatistical Summary:")
print(penguins.describe())


# -------------------------------
# Analyze Body Measurements
# -------------------------------

# Plot distribution of body mass
# KDE shows the estimated distribution curve
sns.displot(penguins['body_mass_g'], kde=True)
plt.title("Distribution of Penguin Body Mass")
plt.show()

# Plot distribution of flipper length
sns.displot(penguins['flipper_length_mm'], kde=True)
plt.title("Distribution of Flipper Length")
plt.show()

# Boxplot helps identify possible outliers
sns.boxplot(data=penguins, x='body_mass_g')
plt.title("Body Mass - Outlier Analysis")
plt.show()


# -------------------------------
# Compare Penguin Species
# -------------------------------

# Boxplot compares body mass across species
sns.boxplot(data=penguins,
            x='species',
            y='body_mass_g')

plt.title("Body Mass by Penguin Species")
plt.show()


# -------------------------------
# Study Relationships
# -------------------------------

# Pairplot shows relationships among numerical variables
sns.pairplot(
    penguins[
        ['flipper_length_mm',
         'bill_length_mm',
         'bill_depth_mm',
         'body_mass_g']
    ],
    kind='reg'
)

plt.show()


# -------------------------------
# Correlation Analysis
# -------------------------------

# Calculate correlation among numerical columns
correlation = penguins[
    ['flipper_length_mm',
     'bill_length_mm',
     'bill_depth_mm',
     'body_mass_g']
].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Display correlation using a heatmap
# annot=True displays correlation values inside cells
sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")
plt.show()

# Find average body mass for each species
print("\nAverage Body Mass by Species:")
print(
    penguins.groupby('species')['body_mass_g']
    .mean()
)




'''Question 4: Use-Case: Hospital Helpdesk Chat Analysis Using Regular Expressions
A hospital receives patient-support messages through an online helpdesk. The system needs to automatically extract patient ID, phone number, email address, and appointment number from the messages.
Consider these chats:
import re

chat1 = "Hello, my patient ID is P10245. Please call me at 9876543210."

chat2 = "I want to reschedule my appointment APT45821. My email is ravi@gmail.com."

chat3 = "My patient ID is P20567 and my contact number is 9123456780. Email: priya@yahoo.com"
Task
Write a Python program using Regular Expressions to:
1.	Extract the 10-digit phone number from chat1 and chat3. 
2.	Extract the patient ID beginning with P followed by digits. 
3.	Extract the appointment number beginning with APT followed by digits. 
4.	Extract the email address from chat2 and chat3. 
5.	Create a reusable function:
'''

import re

chat1 = "Hello, my patient ID is P10245. Please call me at 9876543210."

chat2 = "I want to reschedule my appointment APT45821. My email is ravi@gmail.com."

chat3 = "My patient ID is P20567 and my contact number is 9123456780. Email: priya@yahoo.com"


# Reusable function to extract information
def extract_details(chat):
    patient_id = re.findall(r'\bP\d+\b', chat)
    phone_number = re.findall(r'\b\d{10}\b', chat)
    appointment_number = re.findall(r'\bAPT\d+\b', chat)
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', chat)

    return patient_id, phone_number, appointment_number, email


# Extract details from chat1
patient_id, phone, appointment, email = extract_details(chat1)

print("Chat 1:")
print("Patient ID:", patient_id)
print("Phone Number:", phone)
print("Appointment Number:", appointment)
print("Email:", email)


# Extract details from chat2
patient_id, phone, appointment, email = extract_details(chat2)

print("\nChat 2:")
print("Patient ID:", patient_id)
print("Phone Number:", phone)
print("Appointment Number:", appointment)
print("Email:", email)


# Extract details from chat3
patient_id, phone, appointment, email = extract_details(chat3)

print("\nChat 3:")
print("Patient ID:", patient_id)
print("Phone Number:", phone)
print("Appointment Number:", appointment)
print("Email:", email)













