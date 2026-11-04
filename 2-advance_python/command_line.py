# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:40:11 2026

@author: Admin
"""
#25 july 2026 saturday
import sys
#Function to add two numbers

def add(a, b):
    return a + b

# Read command line arguments
a = int(sys.argv[1])
b = int(sys.argv[2])

#display the result
print( "Answer" , add(a, b))

# Display all command line arguments
print("\nCommand Line Arguments: ")
print( "Program Name:", sys.argv[0])
print( "First Argument Given:", sys.argv[1])
print( "Second Argument Given :", sys.argv[2])



Get Code Through Strings
I: Farah is one of the few associates
in Global Safe Lockers Corp Limited,
who has access to the company 's exclusive Locker that holds
confidential information related to her division.
The PIN to the locker gets changed everv two dqvs.
Farah receives the PIN in the form of Östring :
which she needs to decode to get the single-digit numeric PIN.
The numeric PIN can be obtained by adding the
Lengths of each word of the string to get the total Length,
and then continuously adding the digits of the total Length
till we get a single digit.
For example, if the string is 'iWipro Technologies", 1
the numeric PIN wiLL be 8.