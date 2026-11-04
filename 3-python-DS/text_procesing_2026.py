# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:40:46 2026

@author: Admin
"""

#\d\d\d\d\d\d\d\d\d\d

import re
chat1='Hi: you ask lot of questions   1235678912, abc@xyz.com'
pattern=r'\d\d\d\d\d\d\d\d\d\d'
matches=re.findall(pattern,chat1)
print(matches[0])


chat1='Hi: you ask lot of questions   1235678912, abc@xyz.com'
pattern=r'\d{10}'
matches=re.findall(pattern,chat1)
print(matches[0])


chat2 = 'Hi: here it is: (123)-567-8912, abc@xyz.com'
pattern=r'(\((\d{3})\)-(\d{3})-(\d{4}))'
matches=re.findall(pattern,chat2)
print(matches[0][0])


import re
chat3= 'Hi: Hello, I am having an issue with my order # 412889912'
pattern = r'order[^\d]*(\d*)'  #you will get only digit
matches=re.findall(pattern,chat3)
print(matches[0])


import re
chat4= 'Hi: I have a problem with my order number 412889912'
pattern = r'order[^\d]*(\d*)'  #you will get only digit
matches=re.findall(pattern,chat4)
print(matches[0])


chat5= 'My order 412889912 is having an issue, I was charged 300$ when online it says 280$'
pattern = r'order[^\d]*(\d*)'  #you will get only digit
matches=re.findall(pattern,chat5)
print(matches[0])



chat6= 'Hi: you ask lot of questions   1235678912, abc@xyz.com'
pattern = r'[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*'  #you will get only digit
matches=re.findall(pattern,chat6)
print(matches[0])

####
import re
chat1 ='Hi: Hello, I am having an issue with my order # 412889912'
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
    
matches = get_pattern_match(r'order[^\d]*(\d*)', chat1)
print(matches)


#retrive email id and phone
chat1 = 'Hi: you ask lot of questions   1235678912, abc@xyz.com'
chat2 = 'Hi: here it is: (123)-567-8912, abc@xyz.com'
chat3 = 'Hi: yes, phone: 1235678912 email: abc@xyz.com'
get_pattern_match(r'[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match(r'[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match(r'[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)

#-------phonde number-----
result=get_pattern_match(r'(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
print(result[0])
result=get_pattern_match(r'(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
print(result[1])
result=get_pattern_match(r'(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat3)
print(result[0])


#text is taken from wikipedia
# Store the given information in a multi-line string

text = '''
Born	Elon Reeve Musk
June 28, 1971 (age 55)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa (1971–present)
Canada (1971–present)
United States (2002–present)
Education	University of Pennsylvania (BS, BA)
Title	
Founder, CEO and Chief Engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
Spouse(s)	
Justine Wilson

(m. 2000; div. 2008)
Talulah Riley

(m. 2010; div. 2012)

(m. 2013; div. 2016)
'''

# 1 extract the age

get_pattern_match(r'age (\d+)', text)


#2 extract the name after born
get_pattern_match(r'Born(.*)\n', text).strip()


#3 extract the date of birth
get_pattern_match(r'Born.*\n(.*)\(age', text).strip()

# Let's understand this pattern step by step:
#
# Born       -> Find the word "Born"
# .*         -> Match everything after "Born" on that line
# \n         -> Move to the next line
# (.*)       -> Capture everything on the next line
# \(age      -> Look for the literal text "(age"
#
# In our text:
#
# Born    Elon Reeve Musk
#         ↓
# June 28, 1971 (age 50)
# ^^^^^^^^^^^^^
# This part is captured
#
# Output:
# 'June 28, 1971 ' 
#
# .strip() removes the extra space at the end.
#
# Final output:
# 'June 28, 1971'

#4 extract place of birth

get_pattern_match(r'\(age.*\n(.*)', text)
# Let's break it down:
#
# \(       -> Match the literal opening bracket "("
# age      -> Match the word "age"
# .*       -> Match everything after "age" on the same line
# \n       -> Move to the next line
# (.*)     -> Capture everything on the next line
#
# In our text:
#
# June 28, 1971 (age 50)
#                         ↓
# Pretoria, Transvaal, South Africa
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# This entire line is captured.
#
# Output:
# 'Pretoria, Transvaal, South Africa'

######
def extract_personal_information(text):
    age = get_pattern_match(r'age (\d+)', text)
    full_name = get_pattern_match(r'Born(.*)\n', text)
    birth_date = get_pattern_match(r'Born.*\n(.*)\(age', text)
    birth_place = get_pattern_match(r'\(age.*\n(.*)', text)
    return {
        'name': full_name.strip(),
        'age': int(age),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
        }
extract_personal_information(text)

################################
text = '''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 64)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Stanford University (drop-out)
Occupation	Chairman and MD, Reliance Industries
Spouse(s)	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent(s)	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''

# 1 extract the age

get_pattern_match(r'age (\d+)', text)

#2 extract the name after born
get_pattern_match(r'Born(.*)\n', text).strip()


#3 extract the date of birth
get_pattern_match(r'Born.*\n(.*)\(age', text).strip()



#4 extract place of birth

get_pattern_match(r'\(age.*\n(.*)', text)

######
def extract_personal_information(text):
    age = get_pattern_match(r'age (\d+)', text)
    full_name = get_pattern_match(r'Born(.*)\n', text)
    birth_date = get_pattern_match(r'Born.*\n(.*)\(age', text)
    birth_place = get_pattern_match(r'\(age.*\n(.*)', text)
    return {
        'name': full_name.strip(),
        'age': int(age),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
        }
extract_personal_information(text)

#############
text1 = """Breaking News: Market hits record high
Published on: 2025-08-30
Author: John Doe
In today’s financial update, the stock market closed at an all-time high..."""
 #1 headline
 
headline = re.search(r"Breaking News:\s*(.*)", text1).group(1)
print("Headline:", headline)


### Step-by-step explanation

#### 1. `text1`


text1 = """Breaking News: Market hits record high
Published on: 2025-08-30
Author: John Doe
In today’s financial update, the stock market closed at an all-time high..."""
```

This is a **multi-line string** containing a news article.

The first line is:


Breaking News: Market hits record high

We want to extract only:

text
Market hits record high


### 2. `re.search()`

re.search(r"Breaking News:\s*(.*)", text1)

`re.search()` looks for the **first location in the string where the regular expression matches**.

The pattern is:

Breaking News:\s*(.*)


Let's break it into pieces.

### 3. `Breaking News:`

Breaking News:

This matches the exact text:

text
Breaking News:


So Python first looks for this exact phrase.

### 4. `\s*`


\s*

This is very important.

#### `\s`

Means **whitespace**.

It can match:

* space
* tab
* newline

#### `*`

Means **zero or more times**.

Therefore:


\s*


means:
 Match zero or more whitespace characters.
For example, all of these can be handled:

Breaking News: Market hits record high
Breaking News:    Market hits record high
Breaking News:Market hits record high

This makes the regex flexible.


### 5. `(.*)`

This is the part that **captures the headline**.

#### `.`

means:

 Match any character except newline by default.

#### `*`

means:

 Match zero or more characters.

Therefore:

.*

means:

 Match all characters until the end of the current line.

The parentheses:


(.*)


create a **capturing group**.

So it captures:

text
Market hits record high


### 6. What does `re.search()` return?

Conceptually:


re.search(r"Breaking News:\s*(.*)", text1)


finds:

text
Breaking News: Market hits record high

But the captured group is:

text
Market hits record high

We can see both using:


match = re.search(r"Breaking News:\s*(.*)", text1)

print(match.group(0))
print(match.group(1))


Output:

text
Breaking News: Market hits record high
Market hits record high

### Difference between `group(0)` and `group(1)`

| Expression | Meaning                     |
| ---------- | --------------------------- |
| `group(0)` | Entire matched text         |
| `group(1)` | First captured group `(.*)` |

So:

.group(1)

is used because we don't want:


Breaking News:


###########
Q2. E-commerce product listing
text2 = """Product: Wireless Mouse
Price: $15.99
Rating: 4.5 out of 5

Product: Gaming Keyboard
Price: $45.50
Rating: 4.7 out of 5

Product: Laptop Stand
Price: $29.99
Rating: 4.2 out of 5"""

#1 product
products = re.findall(r"Product:\s*(.*)", text2)

# 2 prices
prices = re.findall(r"\$(\d+\.\d{2})", text2)


# 3 ratings
ratings = re.findall(r"Rating:\s*([\d\.\d]+)", text2)

print("Products:", products)
print("Prices:", prices)
print("Ratings:", ratings)



'''
| Requirement | Regex                 | Meaning                                     |
| ----------- | --------------------- | ------------------------------------------- |
| Product     | `Product:\s*(.*)`     | Extract everything after `Product:`         |
| Price       | `\$(\d+\.\d{2})`      | Extract dollar amount with 2 decimal places |
| Rating      | `Rating:\s*([\d\.\d]+)` | Extract numeric rating                      |
| `\d`        | Digit                 | 0–9                                         |
| `\s`        | Whitespace            | Space/tab/newline                           |
| `*`         | 0 or more             | Optional/repeated                           |
| `+`         | 1 or more             | One or more                                 |
| `.`         | Any character         | Except newline by default                   |
| `\.`        | Literal dot           | Actual `.`                                  |
| `\$`        | Literal dollar        | Actual `$`                                  |
| `( )`       | Capturing group       | Extract this portion                        |
| `[ ]`       | Character class       | Match one of the specified characters       |

'''


#########################################################


text3 = """Job Title: Data Scientist
Company: AI Solutions Pvt Ltd
Location: Pune, India
Posted on: 2025-08-25

Job Title: Machine Learning Engineer
Company: Tech Innovators
Location: Bangalore, India
Posted on: 2025-08-20

Job Title: Business Analyst
Company: DataVision
Location: Hyderabad, India
Posted on: 2025-08-18"""


#1 job title
job_title = re.findall(r"Job Title:\s*(.*)",text3)

#2 company names
companies = re.findall(r"Company:\s*(.*)",text3)

#3dates

dates = re.findall(r"Posted on:\s*(\d{4}-\d{2}-\d{2})",text3)

print("Job Titles:", job_title)
print("Companies:", companies)
print("Dates:", dates)














