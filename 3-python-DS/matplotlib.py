# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:49:45 2026

@author: Admin
"""

import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')
tips.head()
tips.dtypes
tips.describe()

'''inference :
there is min bill of dollers 3 and max bill is 50 dollers
average bill received on counter is 19.31
minimum tip was received ts 1 doller
max tip 10
mtn size of group I
max size 6
average size 2'''


sns.displot(tips.total_bill)
sns.displot(tips.total_bill,kde=True)
#kde=kernel density function
#The distribution is right-skewed
#(positively skewed)—meaning most
#total bills are on the lower side (left),
#but there are a few large bills that stretch
# the distribution to the right.
#This is typical in restaurant or service data,
#where most meals fall within an average range,
#but a few parties may spend much more.
sns.displot(tips.tip,kde=True)
'''inference:usually tip received is in range 2 to 4 dollers
in exception tip is received ts 8-10 dotters
This is right skewed data
'''
sns.displot(tips['size'], kde=True)

sns.jointplot(x=tips.tip,y=tips.total_bill)
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='reg')

'''Scatter PLOt (Center) :
Each point represents one observation
(a customer's bill and the corresponding tip).
There's a positive correlation: as the tip
increases, the total bill tends to increase as well.
However, the increase is not perfectly
linear—some variation exists,
especially for higher bills.
Histogram on the X-axis (Top) :
Shows the distribution of tip amounts.
Most tips fall between $2 and $4,
with fewer tips at the higher end.
Histogram on the Y-axis (Right):
Shows the distribution of totaL_biLL.
The majority of bills are in the $10—$20 range.
'''
#12 august 2026 wednesday
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='hex')
sns.pairplot(tips,kind='reg')

'''total _ bill vs tip
Positive correlation: As the total bill increases,
the tip amount generally increases.
The points are fairly spread,
but there's a visible upward trend.

total bill vs size
Weak positive correlation: Larger group sizes tend
to have higher total bills.

Still, there's a Lot of overlap—small
groups can also have high bills.
tip vs size
Weak correlation: Bigger groups don 't always
give higher tips.
Most tips even in larger groups
still hover around $2-$5.'''

##most of customers are coming for Minner and 50 % are coming lunch
sns.pairplot(tips,hue='time')
'''
Variable-wise Insights:
I. totaL_biLI Distribution (Top-left) :
Dinner bills are generaLLy higher than Lunch bills'''

sns.pairplot(tips,hue='day')

'''
total bill Distribution:
Saturday (green) shows a wider spread and higher peak tn
total bills — more people spending higher amounts.

Friday (orange) has the Lowest density,
suggesting fewer transactions.

tip Distribution:
Saturday and Sunday have more high tips than Thursday
and Friday.'''


sns. heatmap (tips.corr(numeric_only=True),annot=True)
'''Understanding Correlation Coefficients
Ranges from -l to +1.
+1 perfect positive correlation (both increase together).
-i no correlation.
-1 perfect negative correlation (one increases, the other decreases
'''


sns.boxplot(tips['total_bill'])
#There are outliers in total bill
sns.boxplot(tips['tip'])
#There are outliers
sns.boxplot(tips['size'])
     
#categorial variables       
sns.countplot(tips.day)


'''
Mostly cutomers are coming on sat and sunday and Thursday
Very few customers are coming on Friday
'''

sns.countplot(tips.time)
#mostly customers are coming for dinner than Lunch
tips.time.value_counts()
#mostly customers are coming for dinner than Lunch
sns.countplot(tips.sex)
#more male customers are coming compared to female

tips.sex.value_counts().plot(kind='pie')
tips.sex.value_counts().plot(kind='bar')

sns.countplot(data=tips[tips.time=='Dinner'], x='day')

#for dinner, most of customers are coming on sat and sunday
#ver few cutomers are coming for dinner Thu and Friday

sns.countplot(data=tips[tips.time=='Lunch'], x='day')

#most of customers are coming for lunch on Thu and Fri and there are
#coming Sat and Sun
fg=sns.FacetGrid(tips,row='smoker',col='time')
fg.map(sns.histplot,'total_bill')

'''
This ts a facet grid of histograms
showing the distribution of total bills
across different smoking statuses and time of day
(Lunch vs Dinner).
Top-left: Smokers during Lunch
Top-right: Smokers during Dinner
Bottom-left: Non-smokers during Lunch
Bottom-right: Non-smokers during Dinner
Smokers vs. Non-Smokers
Dinner (Top-right vs Bottom-right) :
Both smokers and non-smokers show similar bill
patterns, with peaks between $15— 25.
Smokers have a slightly more spread-out
distribution, indicating more variabil ity.

Lunch (Top-Left vs Bottom-left):
Non-smokers (bottom-left) make up the majority
of Lunch patrons.
Smokers (top-left) are much fewer at lunch,
with total bills mostly under $20.
Lunch vs. Dinner
Dinner is clearly more popular regardless
of smoking status.
Total bills are generally higher and
more varied at dinner, especially for smokers.
'''
##using matplotlib

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#load dataset
tips = sns.load_dataset('tips')

#1. histogram of total_bill
plt.hist(tips['total_bill'], bins=20, color='skyblue', edgecolor='black')
plt.title('total bill distribution')
plt.xlabel('total bill')
plt.ylabel('count')
plt.show()


#######
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import seaborn as sns
tips=sns.load_dataset('tips')
#extract data
data = tips['total_bill']
#perform KDE
density = gaussian_kde(data)
x = np.linespace(min(data), max(data), 200)
y = density(x)

#plot histogram(normalized to density)
plt.hist(data, bins=20, color='skyblue', edgecolor='black',density=True,alpha=0.6)

#plot density curve
plt.plot(x,y, color='blue', linewidth=2)
#labels
plt.title('total bill distribution with density curve')
plt.xlabel('total bill')
plt.ylabel('density')
plt.show()


#2 histogram of tip
plt.hist(tips['tip'], bins=20, color='lightgreen', edgecolor='black')
plt.title('tip distribution')
plt.xlabel('tip')
plt.ylabel('count')
plt.show()

#3scatter plot of tip vs total_bill

plt.scatter(tips['tip'], tips['total_bill'], color='purple', alpha='0.6')
plt.title('tip vs total bill')
plt.xlabel('tip')
plt.ylabel('total bill')
plt.show()

#13 august 2026 thursday

#4 simple coorelation matrix

corr = tips.corr(numeric_only=True)
corr
plt.imshow(corr, cmap='coolwarm', interpolation='none')

#With interpolation=None each grid cell is drawns as solid square
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation=45)

'''
With interpolation=None each grid cell is drawns as solid square
plt.xticks(...)
This function controls the labels on the x-axis:
Where the ticks are placed.
What labels are shown.
How the labels are rotated or styled.
range(len(corr))
This generates the positions for the ticks:
corr is a square matrix (like 3x3 if there are 3 
                         numeric columns).

len(corr) gives how many columns (and rows) there are,
 say: 3.
range(len(corr)) → [0, 1, 2] → places ticks at positions 0, 1, and 2.
corr.columns
These are the labels for those tick positions:
['total_bill', 'tip', 'size']
So now you’re labeling tick 0 as "total_bill", tick 1 as "tip", etc.
'''
plt.yticks(range(len(corr)), corr.columns)
plt.title('correlation matrix')
plt.show()


#5.boxplots
plt.boxplot(tips['total_bill'])
plt.title('boxplot - total bill')
plt.show()

plt.boxplot(tips['tip'])
plt.title('boxplot - tip')
plt.show()


#6 count of days

tips['day'].value_counts().plot(kind='bar', color='orange')
plt.title('count by day')
plt.xlabel('day')
plt.ylabel('count')
plt.show()

#7 count of gender

tips['sex'].value_counts().plot(kind='bar', color='lightblue')
plt.title('count by gender')
plt.xlabel('sex')
plt.ylabel('count')
plt.show()


#8 gender pie chart
tips['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%')

'''
The autopct='%1.1f%%' parameter is used in
 Matplotlib's pie() function to display the 
 percentage value on each slice of a pie chart.

Breakdown of '%1.1f%%':
% starts a formatting string.
1.1f means:
1 = minimum width of the number (not strictly needed here).
.1f = format the number as a float with 1 decimal place.
The final %% is to display a literal percent sign % 
(because % has special meaning in formatting strings, 
 so we escape it with another %).
Example:
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C']
sizes = [30, 45, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')  # Keeps the pie chart circular
plt.show()
'''

plt.title('gender distribution')
plt.ylabel('')
#Even though pie charts don't use a y-axis,
#MatpIotIib still has that axis object in the
# background. So setting ylabel('')just makes
#sure nothin is dis la ed there.
plt.show()













































































































