# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:47:34 2026

@author: Admin
"""

#30 july 2026, thursday

import pandas as pd
f1=pd.read_csv('age.csv')


f1=pd.read_csv('c:/3-python-DS/age.csv')
f1


df=pd.read_excel('c:/3-python-DS/Bahaman.xlsx')


#a numpy array
import numpy as np
numpy_ser = np.array([145, 142, 38, 13])
print(songs3.iloc[1])
#142
print(numpy_ser[1])

#they both have methods in comman
songs3.mean()
print(numpy_ser.mean())



#
import pandas as pd
george= pd.Series([10, 7, 1, 22],
index=['1968', '1969', '1970', '1970'],
name='george_songs'
)
george

george.loc['1968']

george['1970']
for item in george:
    print(item)
#updating

george['1969'] = 68
george['1969']
george

#deletion
s = pd.Series([2,3,4], index=[1,2,3])
s
del s[1]
s

#converting datatypes

#Convert Types
#string use. astype(str)
#numeric use pd.to numeric
#integer use .astype(int),
#note that this will fail with NaN
#datetime use pd.to_datetime
import pandas as pd
songs_66 = pd.Series([3, None , 11, 9],
index=['qqwew', 'ekdf', 'fjdf', 'ffef'],
name='Counts'                 
                     )

#dtype(float64)
songs_67 = pd.Series([3, None , 11, 9],
index=['qqwew', 'ekdf', 'fjdf', 'ffef'],
name='Counts',
dtype="Int64" 

)
print(songs_67)
print(songs_67.dtypes)


pd.to_numeric(songs_66.apply(str))

pd.to_numeric(songs_66.astype(str), errors='coerce')

songs_66.dtypes
#fillna
songs_66 = pd.Series([3, None , 11, 9],
index=['qqwew', 'ekdf', 'fjdf', 'ffef'],
name='Counts' )                
print(songs_66.dtypes)
songs_66=songs_66.fillna(-1)
songs_66
songs_66=pd.to_numeric(songs_66.apply(str))
print(songs_66.dtypes)



#
songs_66=songs_66.fillna(-1)
songs_66=songs_66.apply(str)
print(songs_66.dtypes)

#or
songs_66=songs_66.fillna(-1).astype(str)
print(songs_66.dtypes)

#
songs_66 = pd.Series([3, None , 11, 9],
index=['qqwew', 'ekdf', 'fjdf', 'ffef'],
name='Counts' )                
songs_66=songs_66.dropna()
songs_66

##append joining two series
songs_66 = pd.Series([3, None , 11, 9],
index=['qqwew', 'ekdf', 'fjdf', 'ffef'],
name='Counts' )                

songs_69 = pd.Series([7, 16 , 21, 39],
index=['ram', 'sham', 'harshu', 'ashu'],
name='Counts' )                

songs=pd.concat([songs_66,songs_69])
songs

##plotting series
import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot()
plt.legend()

###
fig = plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar', color='r')
plt.legend()

































