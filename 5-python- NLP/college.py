# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:26:56 2026

@author: Admin
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "College": ["JSPM", "PICT", "MIT", "PCCOE", "Wadia"],
    "Computing": [4.2, 4.8, 4.6, 4.5, 4.0],
    "Skills": [4.0, 4.7, 4.4, 4.3, 3.8],
    "Professors": [4.3, 4.6, 4.5, 4.4, 4.1],
    "Placement": [4.1, 4.9, 4.3, 4.6, 3.7]
}


df = pd.DataFrame(data)


sns.set_theme(style="whitegrid")


plt.figure(figsize=(10, 12))


plt.subplot(3, 1, 1)

df.plot(
    x="College",
    kind="bar",
    ax=plt.gca()
)

plt.title("College Comparison")
plt.xlabel("College")
plt.ylabel("Rating")
plt.ylim(0, 5)
plt.legend(title="Parameters")


plt.subplot(3, 1, 2)

sns.heatmap(
    df.set_index("College"),
    annot=True,
    cmap="YlGnBu",
    fmt=".1f"
)

plt.title("College Performance Heatmap")
plt.xlabel("Parameters")
plt.ylabel("College")


plt.subplot(3, 1, 3)

for column in df.columns[1:]:
    plt.plot(
        df["College"],
        df[column],
        marker="o",
        label=column
    )

plt.title("College Performance")
plt.xlabel("College")
plt.ylabel("Rating")
plt.ylim(3.5, 5)
plt.legend(title="Parameters")


plt.tight_layout()


plt.show()