# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 18:38:27 2026

@author: Admin
"""

#28 july 2026 tuesday
'''Get Code Through Strings - 1: Farah is one of the few associates
 in Global Safe Lockers Corp Limited, 
 who has access to the company's exclusive locker that holds 
 confidential information related to her division. 
 The PIN to the locker gets changed every two days.
 Farah receives the PIN in the form of a string 
 which she needs to decode to get the single-digit numeric PIN.

The numeric PIN can be obtained by adding the
 lengths of each word of the string to get the total length,
 and then continuously adding the digits of the total length 
 till we get a single digit.

For example, if the string is "Wipro Technologies", 
the numeric PIN will be 8.

Explanation:
Length of the word "Wipro" = 5

Length of the word "Technologies" = 12

Let us add all the lengths to get the Total Length = 5 + 12 = 17

The Total Length = 17, which is not a single-digit, 
so now let us continuously add all digits till 
we get a single digit i.e. 1 + 7 = 8

'''

input1 = "wipro technoogies"

#step1: split into wprds
words = input1.split()
#['wipro', 'technologies']
words
#step2: convert words into lists of chracters
char_lists = [list(word) for word in words]
#[['w','i','p','r','o',],]

char_lists






##[5,12]
print("character lists:", char_lists)
print("letter counts:", letter_counts)
def sum_digit(num):
    total = 0
    while num!=0:
        last


'''
Test Case 1 (Already done)
Input: "Wipro Technologies"
Splits into: 2 words → lengths = [5, 12]
Sum of digits = [5, 3]
Final total = 8
 Test Case 2
Input: "Apple Banana"
Split → ['Apple', 'Banana']
Lengths → [5, 6]
Digit Sums → [5, 6]
Final total = 11=2

 Test Case 3
Input: "Data Science and AI"
Split → ['Data', 'Science', 'and', 'AI']
Lengths → [4, 7, 3, 2]
Digit Sums → [4, 7, 3, 2]
Final total = 16=7
 Test Case 4
Input: "BigData Analytics MachineLearning"
Split → ['BigData', 'Analytics', 'MachineLearning']
Lengths → [7, 9, 15]
Digit Sums → [7, 9, 1+5 = 6]
Final total = 22=4
 Test Case 5 (Single word)
Input: "Python"
Split → ['Python']
Lengths → [6]
Digit Sum → [6]
Final total = 6
'''
'''
Corner cases (also called edge cases) are unusual or extreme 
input scenarios that test the limits of your program.
 These are situations where the input might be:
Empty
Very large or very small
Unexpected in format
On the boundary of acceptable input
They are important because they help ensure
 your code doesn't break or behave incorrectly 
 under unexpected conditions.
'''
#Corner Case 1: Empty String
input1 = ""
#split() → []

#No words, so char_lists = [], letter_counts = [], total = []

#total_sum = 0
#Corner Case 2: Only Spaces
input1 = "     "
#split() → still [] (all spaces trimmed)
#Same outcome as above

# Expected Output: total_sum = 0

#Corner Case 3: Special Characters or Numbers in Words
input1 = "AI 101 @Home"
#split() → ['AI', '101', '@Home']
#Lengths → [2, 3, 5]
#Sum of digits → [2, 3, 5]
#Final sum → 10

#Handles non-letter characters because it's based on character count, not character type.

#step 4: apply sum_digits to each word length
total






'''
Simple Encoded Array_1: Maya has stored few confidential 
numbers in an array (array of int). To ensure that others do not find
 the numbers easily, she has applied a simple encoding.S
Encoding used: Each array element has been substituted with a 
value that is the sum of its original value and its succeeding element's
 value.
i.e. arr[i] = original value of arr[i] + original value of arr[i+1]
e.g. value in arr[0] = original value of arr[0] + original value of arr[1]
Also note that value of last element i.e. arr[last index] remains unchanged.
Example:
If the encoded array is {7,6,8,16,12,3}
The original array should have been {2,5,1,7,9,3}

'''
def getOriginalArray(input1,input2):
    original=[0]*input2
    original[-1]=input1[-1]
    #Extracting from encoded array
    for i in range(input2-2,-1,-1):
        original[i]=input1[i]-original[i+1]
    return original,sum(original)
input1=[7,6,8,16,12,3]
input2=len(input1)
getOriginalArray(input1,input2)

#This is a for loop in Python, and 
            #the range(start, stop, step) function defines how it loops:
            #start = input2 - 2 → This is the second last index of the array.
            #stop = -1 → This is the ending condition, not inclusive. Since we are going backwards, we stop when i becomes less than 0.
            #step = -1 → This means we are going in reverse, moving from right to left.
            #This means: go backward from second last element 
            #to first.
            #Why is -1 used?
            #Because range stops just before the stop value.
            #So if we want to include index 0, we write -1 as the
            #stop value.
            #Why input2-2?
             #Because:You already set the last element: original[-1] = input1[-1]
             #So now you want to fill the rest of the array 
             #from second-last to first, using the encoded logic.


'''
            Let’s do it step-by-step for:
                input1 = [7, 6, 8, 16, 12, 3]
                Iteration Steps:
                i = 4: original[4] = 12 - 3 = 9
                [0, 0, 0, 0, 9, 3]
                i = 3: original[3] = 16 - 9 = 7
                 [0, 0, 0, 7, 9, 3]
               i = 2: original[2] = 8 - 7 = 1
               [0, 0, 1, 7, 9, 3]
               i = 1: original[1] = 6 - 1 = 5
               [0, 5, 1, 7, 9, 3]
               i = 0: original[0] = 7 - 5 = 2
               [2, 5, 1, 7, 9, 3]
            
            '''
            



#29 july 2026 wednesday

'''
Decreasing sequence: Given an integer array, find the number 
of decreasing sequences in the array and the 
length of its longest decreasing sequence.
You are expected to complete the logic within the given function, where:
input1 represents the integer array, and
input2 represents the number of elements in the integer array.
The function should set the output1 variable to the number of 
decreasing sequences in the array and 
set the output2 variable to the length of the longest decreasing sequence in the array.

Example 1:
If input1 = {11,3,1,4,7,8,12,2,3,7}
and input2 = 10

output1 should be 2,3


'''
#count the number of decreasing sequence and max_length
input1 = [11, 3, 1, 4, 7, 8, 12, 2, 3, 7]
def count_decreasing_sequence(input1):
    
    input2 = len(input1)
    
    count_sequence = 0 #number of dercresing sequence
    max_length = 0 #longest sequence length
    current_length = 1 #start with 1
    
    for i in range(1, input2):# strat from second element
        if input1[i] < input1[i - 1]: # if its decresing
            current_length += 1 # increse sequence length
        else:
            if current_length > 1: # if we had decresing sequence
                count_sequence += 1
                max_length = max(max_length, current_length)
                current_lenght = 1
                
# final check for last sequence
    if current_length > 1:
        count_sequence += 1
        max_length = max(max_length, current_length)
    return count_sequence,max_length

print(count_decresing_sequence(input1))

print(count_decresing_sequence([11, 3, 1, 4, 7, 8, 12, 2, 3, 7]))


print(count_decresing_sequence([1, 2, 3, 4]))


print(count_decresing_sequence([10, 9, 8, 7]))


print(count_decresing_sequence([5, 3, 4, 2, 6,1]))

print(count_decresing_sequence([100]))


#corner case1 : empty list

print(count_decresing_sequence([]))
#o/p: (0,0)
#explanation: no numbers -> no sequence

#corner case2 : single element
print(count_decresing_sequence([5]))


#corner case1 : all elements same
print(count_decresing_sequence([4, 4, 4, 4]))

#corner case1 : empty list
print(count_decresing_sequence([9, 8, 7, 6, 5]))




'''

Sum of Powers of Digits_1: Alex has been asked by his teacher 
to do an assignment on powers of numbers.
 The assignment requires Alex to find the 
 sum of powers of each digit of a given number, 
 as per the method mentioned below.

If the given number is 582109, the Sum of Powers of Digits will be calculated as:
= (5 raised to the power of 8) + 
(8 raised to the power of 2) + 
(2 raised to the power of 1) + 
(1 raised to the power of 0) +
 (0 raised to the power of 9) + 
 (9 raised to the power of 0)

i.e. each digit of the number is raised to the power of the next digit on its right side.
Note that the right-most digit has to be raised to the power of 0. The sum of all of these powers is the expected result to be calculated.

Example - If the given number is 582109, the Sum of Powers of Digits =
= (5 raised to the power of 8) + (8 raised to the power of 2) + (2 raised to the power of 1) + (1 raised to the power of 0) + (0 raised to the power of 9) + (9 raised to the power of 0)
= 390625 + 64 + 2 + 1 + 0 + 1 = 390693

Alex contacts you to help him write a program for finding the Sum of Powers of Digits for any given number, using the above method.

Write the logic in the given function sumOfPowerOfDigits
 where,
input1 represents the given number.
The function is expected to return 
the "Sum of Powers of Digits" of input1


'''

def sumOfPowerofDigits(input1):
    num_str =str(input1) #convert the number to a string for eashy 
    ''' the input number (input ) is converted to a string num_str,
    so we can acesss each digit easily using indexing.
    example if input  = 582109 then num_ster="582109"
    '''
    total_sum=0
    
    for i in range(len(num_str)):
        base = int(num_str[i])
        
        if i + 1 < len(num_str):
            exponent = int(num_str[i + 1])
        else:
            exponent = 0
        total_sum +=base ** exponent
        
    return total_sum

test_number=582109
print(sumOfPowerofDigits(test_number))


test_number2=50
print(sumOfPowerofDigits(test_number2))


test_number3=7
print(sumOfPowerofDigits(test_number3))


test_number4=204
print(sumOfPowerofDigits(test_number4))


test_number5=1111
print(sumOfPowerofDigits(test_number5))

#corner cases

test_number6=987
print(sumOfPowerofDigits(test_number6))


test_number7=105
print(sumOfPowerofDigits(test_number7))


test_number8=1000
print(sumOfPowerofDigits(test_number8))


test_number9=98
print(sumOfPowerofDigits(test_number9))









