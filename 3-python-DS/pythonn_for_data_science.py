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