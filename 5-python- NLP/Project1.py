# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:53:23 2026

@author: Admin
"""

import pandas as pd
data = {
    "College Name": [
        "Savitribai Phule Pune University",
        "JSPM University",
        "Fergusson College",
        "MIT ADT University",
    ],
    "Sufficient Computing Facility": [
        "High (good IT infrastructure )",
        "Moderate (CS computing labs)",
        "Moderate (basic for general Arts)",
        "Very High (Specialized modern labs, cloud systems & Mac labs)",
    ],
    "Imparting Job-Required Skills": [
        "Moderate (domain focus student-driven upskilling)",
        "High (Value-added certifications)",
        "Moderate-High (Strong analytical thinking)",
        "High (project-based learning)",
    ],
    "Sufficient Skilled Professors": [
        "Very High (Senior PhDs, tenure researchers)",
        "Moderate-High (industry visiting experts)",
        "Very High (strong academic pedigree in Arts/Sci)",
        "High (Blend of academic PhDs and corporate practitioners)",
    ],
    "Placement Support Provided": [
        "Moderate-High (Active central placement cell)",
        "High (Dedicated T&P cell, 50+ recruiters)",
        "Moderate (Career Facilitation Center)",
        "High (strong placement drives across streams)",
    ],
}

df = pd.DataFrame(data)
print(df.to_markdown(index=False))



import matplotlib.pyplot as plt

scores = {
    "College": ["SPPU", "JSPM", "Fergusson", "MIT ADT"],
    "Computing Facility": [4, 4, 3, 5],
    "Job Skills": [4, 4, 4, 5],
    "Skilled Professors": [5, 4, 5, 5],
    "Placement Support": [4, 3, 3, 4],
}

score_df = pd.DataFrame(scores)
score_df["Overall Score (Out of 20)"] = score_df.iloc[:, 1:].sum(axis=1)
score_df.plot(
    x="College", y="Overall Score (Out of 20)", kind="bar", legend=False
)
plt.title("Overall College Comparison Score")
plt.ylabel("Score")
plt.show()








