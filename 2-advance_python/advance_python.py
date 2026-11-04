# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:30:43 2026

@author: Admin
"""

##advance python
##15 july 2026

##list comprehension
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

##code optimization
##we can write same method using list comprehension
lst=[num for num in range(0,20)]
print(lst)

#####
names=['dada', 'mama', 'kaka']
lst=[name.capitalize()for name in names]
print(lst)

########list comprehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

####list comprehension for even number code optimization
evens = [num for num in range(10) if num % 2 ==0]
print(evens)

##list comprehension for inside for
lst=[f"{x}:{y}"for x in range(3)for y in range(3) ]
print(lst)

###set comprehension
set_one={ x for x in range(3)  }
print(set_one)
##dictionary comprehension
dict={x:x*x for x in range(3) }
print(dict)

###genrator expression

gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
    
 #########  
gen=(x for x in range(3))
next(gen)
next(gen)

""" Function which returns myltiple vlues
when you call a regualr function it rns immediately and retrun a value
when you call a generator function (a functio with yield
 you then yuse next() or loop (for , etc.) to iterate through 
 the values it yields one by one."""

def range_even(end):
    for num in range(0, end, 2):
        yield num
        
result=range_even(6)
print(result)
for num in result:
    print(num)

##now instead of using for loop we can write our own genartaor
result=range_even(6)
next(result)
next(result)

##let us hide password entered on screen
#chaining generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
 def hide(itr):
     for ele in itr:
         yield ele*'*'
         
       
        
        
passwords=["not-good","give'm-pass","00100=100"]

for password in hide(lengths(password)):
    print(password)


##enumerate
#printing list with index
lst=["milk","egg","bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')

##same code can be implemented using enumerate
lst=["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
    
    
##use of zip function

name=['dada', 'mama','kaka']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

##use of zip function with mismatch list
##it will not display excess mismatch item in name
name=['dada', 'mama','kaka', 'baba']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)
    
##zip longest
from itertools import zip_longest
name=['dada', 'mama','kaka', 'baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

###use of fill value instead none
from itertools import zip_longest
name=['dada', 'mama','kaka', 'baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

#####use of all(),if all the values are
##true then it will produce output
lst=[2,3,-6,8,9]#values must be non zero,+ve or-ve
if all(lst):
    print('all values are true')
else:
    print('there are null values')

############
lst=[2,3,0,8,9]#values must be non zero,+ve or-ve
if all(lst):
    print('all values are true')
else:
    print('there are null values')

####use of any if any one non zero value
lst=[0,0,0,-8,0]
if any(lst):
    print('it has some non zero value')
else:
    print('all values are null in the list.')
####
lst=[0,0,0,0,0]
if any(lst):
    print('it has some  value')
else:
    print('all values are null in the list.')

###count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

##now let us start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))


#16 july 2026
##cycle
##suppose you have repeated tasks to be done then you can

import itertools

instructions=("eat", "code", "sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)


###repeat()

from itertools import repeat
for msg in repeat("keep patience", times=4):
    print(msg)

##combinations()
'''order does not mattder.
used when you are choosing or selecting items,
not arranging them
formula (when selecting r from n):
    C(n, r)=n!/r!(n-r)!
    how many ways can you choose 3 players from a team of 5?
    this is a combination because the order of selection doesn't matter.
    C(5, 3)=5!/3!(5-3)!=120/6X2=120/12=10
    '''

from itertools import combinations
players=


'''permutations
order matters
used when you are arranging or ordering items.
formula
p(n, r)=n!/(n-r)!
'''

from itertools import permutations
players=['john', 'jani', 'janardhan']
for seat in permutations(players,2):
    print(seat)
    
    
#product
    
from itertools import product
team_a=['rohit','pandya','bumrah']
team_b=['virat','manish','sami']   
 for pair in product(team_a,team_b):
  print(pair)
    
 ##
age=[27,17,21,19]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])   

##assignment operation
#this will only create a new variable with the same reference
list_a = [1,2,3,4,5]
list_b = list_a
print('id of old list:', id(list_a))     
print('id of old list:', id(list_b))   
list_a[0] = -10
print(list_a)
print(list_a)

###
old_list = [[1,2,3], [4,5,6], [7,8,'a']] 
new_list = old_list

new_list[2][2] = 9
print('old_list:', old_list)
print('id of old list:', id(old_list))  
print('new_list:', new_list)
print('id of new list:', id(new_list))  
  
    
##shallow copy
import copy
list_a = [1, 2, 3, 4, 5]
list_b = copy.copy(list_a)

#not affect the other list
list_b[0] = -10

print('old list:', list_a)
print('id of old list:', id(list_a))
print('new list:', list_b)
print('id of new list:', id(list_b))
  

###
import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.copy(list_a)
# affect the other list
list_a[0][0] = -10
print(list_a)
print(list_b)
print('id of old list:', id(list_a))
print('id of new list:', id(list_b))
  
##deep copies
import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)
# not affect the other list
list_a[0][0] = -10
print(list_a)
print(list_b)
print('id of old list:', id(list_a))
print('id of new list:', id(list_b))

##
with open('c:/2-advance_python/pi_digits.txt','r') as file:
    #the open() function needs
    #one arguments: the name of the file you want to open.
    contents = file.read()
print(contents)

#observe the extra line at the end of the output
##to avoid this rstrip() method is used
with open('c:/2-advance_python/pi_digits.txt','r') as file:
    #rstrip() methods removes, or strips, any whitespaces
    #chracter from the right side of a string
    contents = file.read()
print(contents.rstrip())

####instead writing absolute path in open(), you can define file_path
file_path='c:/2-advance_python/pi_digits.txt'
with open(file_path) as file:
    contents = file.read()
print(contents.rstrip())

###reading file line by line

file_path='c:/2-advance_python/pi_digits.txt'
#we assign the name of the file we are raeding from to the variable
with open(file_path) as file:
#we again use the with syntax to 
#let pytho open and close
#the file properly
    for line in file:
       print(line)


#rstrip()
file_path='c:/2-advance_python/pi_digits.txt'
with open(file_path) as file:
     for line in file:
         print(line.rstrip())

##making list of lines from files
filename='c:/2-advance_python/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
lines
for line in lines:
    print(line.rstrip())

##working with file contents
filename='c:/2-advance_python/pi_digits.txt'
with open(filename) as file:
    lines = file.readlines()
    pi_strings = ''
    for line in lines:
        pi_strings += line.rstrip()
        print(pi_strings)
        print(len(pi_strings))

####
import pandas as pd
f1=pd.read_csv('buzzers.csv')#relative path
f2=pd.read_csv('C:/2-advance_python/buzzers.csv')#absolute path
print(f2)

#17 july 2026



#21 july 2026
#encoding
text = "मी AIGenius मध्ये skilling करत आहे आणि मला skilling करण्याचा आनंद होत आहे"

# save as utf-8
with open ('sample_utf8.txt', 'w', encoding='utf-8') as f:
    f.write(text)
    
#save as utf-16
with open ('sample_utf16.txt', 'w', encoding='utf-16') as f:
    f.write(text)
    
#save as latin-1 (will replace marathi character)
with open ('sample_latin1.txt', 'w', encoding='utf-8') as f:
    f.write(text)
    

#read with utf-8(most reliable for multilingual text)
with open ('C:/2-advance_python/sample_utf8.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print("UTF-8 Read:\n", data)


#read with utf-16
with open ('C:/2-advance_python/sample_utf8.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print("UTF-8 Read:\n", data)


#read with latin




'''what is BOM (BYTE ORDER MARK)'''

#HANDLING EXCEPTIONS FOR CROSS ENCODING

text = "मी AIGenius मध्ये skilling करत आहे आणि मला skilling करण्याचा आनंद होत आहे"

#save as utf-8
with open ('handling_encoding.txt', 'w', encoding='utf-8') as f:
    f.write(text)
    
#ASCII with error handling
try:
    with open ('handling_encoding.txt', 'r', encoding='ascii') as f:
        data = f.read()
        print("ASCII Read:\n", data)
except UnicodeDecodeError as e:
    print("ASCII Read Failed:", e)


# detect encoding automatically (optional tool)
#you can use the chardet library to guuess
#file encoding:

#imp quick section reference code

import chardet
file_path = "handling_encoding.txt" #replace with your file name

with open(file_path, "rb") as file:
    raw_data = file.read()
    
result = chardet.detect(raw_data)

print("detected encoding :", result["encoding"])
print("confidence        :", result["confidence"])

print(raw_data)

##########UTF-8

file_name = "C:/2-advance_python/sample_utf8.txt"

try:
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.read()
        print("file read successfully!\n")
        print(data)
except FileNotFoundError:
    print(f"file not found:{file_name}")
except UnicodeDecodeError:
    print(f"could not decode '{file_name}' using UTF-8.")

#UTF-16
file_name = "C:/2-advance_python/sample_utf16.txt"

try:
    with open(file_name, "r", encoding="utf-16") as f:
        data = f.read()
        print("file read successfully!\n")
        print(data)
except FileNotFoundError:
    print(f"file not found:{file_name}")
except UnicodeDecodeError:
    print(f"could not decode '{file_name}' using UTF-16.")



###latin
file_name = "C:/2-advance_python/sample_latin1.txt"

try:
    with open(file_name, "r", encoding="latin1") as f:
        data = f.read()
        print("file read successfully!\n")
        print(data)
except FileNotFoundError:
    print(f"file not found:{file_name}")
except UnicodeDecodeError:
    print(f"could not decode '{file_name}' using latin1.")


#ASCII
file_name = "C:/2-advance_python/sample_ascii.txt"

try:
    with open(file_name, "r", encoding="ascii") as f:
        data = f.read()
        print("file read successfully!\n")
        print(data)
except FileNotFoundError:
    print(f"file not found:{file_name}")
except UnicodeDecodeError:
    print(f"could not decode '{file_name}' using ascii.")


#####decorators
####pre-requisite to decorators
def plus




###passing functions as arguments
#to other functions
def plus_one(number):
    result1= number + 1
    return result1
def function_call(function):
    result=function(5)
    return result

function_call(plus_one)




# 22 july 2026
#function returning other functions
def hello_function():
    def say_hi():
        return "hi"
    return say_hi
#hello_function()
hello=hello_function()
hello()
##


##need for decorators
import time
def calc_square(numbers):
    start=time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000 ##output wiil be in mili second
    print(f"total time foe execution square is{total_time}")
    return result

def calc_cube(numbers):
    start=time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000 ##output wiil be in mili second
    print(f"total time foe execution cube is{total_time}")
    return result

array = range(1,1000000)
out_square = calc_square(array)
out_cube = calc_cube(array)


###############3
##a python decorator is a function
##that takes in a function and
#return it by adding some functionality.
def say_hi():
    return 'hello there'
def uppercase_decorator(function):
     def wrapper():
         func = function()
         make_uppercase = func.upper()
         return make_uppercase
     return wrapper
decorate = uppercase_decorator(say_hi)
decorate()
'''however, python provides a much easier way for
us to apply decorators.
we simply use the @ symbol before
the function we'd like to decorate''' 

#############
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def say_hi():
    
say_hi()

'''

'''

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()


#######
import time

def time_it(function):
    # This is a decorator function that takes
    # another function (func) as an argument.

    def wrapper(*args, **kwargs):
        # *args and **kwargs allow wrapper
        # to accept any number of positional and keyword arguments.

        start = time.time()
        result = function(*args, **kwargs)

        # Calls the original function (func)
        # with the provided arguments.

        end = time.time()

        print(function.__name__ + " took " +
            str((end - start) * 1000) + "mil sec")

        return result

    return wrapper


@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


array = range(1, 1000000)

out_square = calc_square(array)
out_cube = calc_cube(array)




###23 july 2026 thursday

###exception handling
a=10
b=0
result =a/b
#throws arithmeticexception: / by zero
#####
##zero division error
try:
    result = a/b
except ZeroDivisionError:
    print("cannot divide by zero")
####
##indexerror
numbers = [1, 2, 3]
print(number[5])

try:
    print(number[5])
except IndexError:
    print("index out of range")
    
    
###handling exception without naming them

try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print ("division performed successfully")
except ValueError:
    print("only integers should be entered")
except:
    print("oops......some exception raised")
    
#"Hand1ing exception using try... except... else"

try:
    numerator=50
    denom=int(input( "Enter the denominator:"))#enter
    quotient=(numerator/denom)
    print ( "Division performed successfully")
except ZeroDivisionError:
    print ("Denominator as ZERO is not allowed")
except ValueError:
    print ( "Only INTEGERS should be entered")
else:
    print ("The result of division operation is", quotient)

###"Hand1ing exception using try... except... else... finally"
try:
    numerator=50
    denom=int(input ("Enter the denominator:"))#enter 10,10.3 n 0
    quotient=(numerator/denom)
    print ("Division performed successfully")
except ZeroDivisionError:
    print ("Denominator as ZERO is not allowed")
except ValueError:
    print( "Only INTEGERS should be entered")
else:
    print( "The result of division operation is", quotient)
finally:
    print( "OVER AND OUT")


#####file not found error

with open( 'c:/10-python/pi_digits1. txt','r') as file:
    contents = file.read()
print (contents . rstrip())
####
try:
    with open( "c:/10-python/pi_digitsI. txt",'r') as file:
content = file.read()
except FileNotFoundError:
print( "File not found!")
file:
"r 




##attribute error
obj = None
print(obj.some_attribute)
####
if obj is not None: 
    print(obj.some_attribute)
else:
    print("object is none")


####memoryerror
huge_list = [1] * (10**10)
###handling using generator
def generate_numbers():
     for i in range(10**10):
         yield i 
         
###recursive function error
def recursive_function():
    return recursive_function()

recursive_function()

###
import sys
sys.setrecursionlimit(1000)

def safe_recursive_function(depth=0, max_depth=10):
    if depth >= max_depth:
        return "done"
    return safe_recursive_function(depth+1, max_depth)
print(safe_recursive_function())

##intial balance

balance = 500

def withdraw(amount) :
    global balance # Allow modification of the global balance
    
    try :
        # Check if the amount is a valid number
        if not isinstance(amount, (int, float)):
            raise TypeError( "Invalid amount type! Please enter a number. ")
            # Check if the amount is negative
        if amount <=0:
            raise valueError( "Withdrawal amount must be greater than zero. ")
                # Check for insufficient balance
        if amount > balance:
            raise valueError( "Insufficient balance!")

        # Deduct amount
        balance -= amount
        print(f"WithdrawaL successful! New balance:${baLance:.2f}")
    except TypeError as e:
        print(f"Error: {e}" )
    except ValueError as e:
        print(f"Transact on Faile.")
except Exception as e:
    print(f"Unexpected Error: {e}")
Test Cases
withdraw(IØØ)
withdraw( "fifty") #
withdraw( -50)
withdraw(10Ø0)
Success
Error: Invalid amount type!
Error: Amount must be greater than zero.
Error: Insufficient balance!

































    

















































































































    
    
    
    
    
    






































































