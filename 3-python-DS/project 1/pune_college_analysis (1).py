
# ============================================================
# PUNE TOP 5 COLLEGES - PYTHON DATA ANALYSIS PROJECT
# ============================================================
# Requirements:
#     pip install pandas numpy matplotlib
#
# Files:
#     pune_colleges.csv
#     pune_college_analysis.py
#
# IMPORTANT:
# - Factual fields (founding year, NAAC grade, NIRF values) were
#   entered from publicly available institutional/NIRF sources.
# - Academic-area 0/1 flags are analysis indicators based on the
#   broad areas represented in the original project brief.
# - Do NOT treat the derived "Breadth Score" as an official ranking.
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ---------- 1. Load data ----------
FILE = Path(__file__).with_name("pune_colleges.csv")
df = pd.read_csv(FILE)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 160)

print("=" * 80)
print("PUNE TOP 5 COLLEGES - OVERALL PYTHON ANALYSIS")
print("=" * 80)

print("\n1) DATASET")
print(df)

# ---------- 2. Basic inspection ----------
print("\n2) SHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n3) DATA TYPES")
print(df.dtypes)

print("\n4) MISSING VALUES")
print(df.isnull().sum())

# ---------- 3. Data cleaning ----------
# Convert NIRF fields to numeric; missing values stay NaN.
df["NIRF_2025_Overall_Rank"] = pd.to_numeric(
    df["NIRF_2025_Overall_Rank"], errors="coerce"
)
df["NIRF_2025_Overall_Score"] = pd.to_numeric(
    df["NIRF_2025_Overall_Score"], errors="coerce"
)

# ---------- 4. Academic area analysis ----------
area_cols = [
    "Arts", "Science", "Commerce", "Research",
    "Engineering", "Management", "Law", "IT", "Medicine", "Design"
]

# Question 1: Which college has the widest academic breadth?
df["Breadth_Score"] = df[area_cols].sum(axis=1)

breadth = df[["College", "Breadth_Score"]].sort_values(
    "Breadth_Score", ascending=False
)
print("\n5) QUESTION 1 - ACADEMIC BREADTH")
print(breadth)

# Question 2: Which academic area is most common?
area_counts = df[area_cols].sum().sort_values(ascending=False)
print("\n6) QUESTION 2 - MOST COMMON ACADEMIC AREAS")
print(area_counts)

# Question 3: Which colleges offer Engineering?
engineering_colleges = df.loc[df["Engineering"] == 1, "College"]
print("\n7) QUESTION 3 - ENGINEERING COLLEGES")
print(engineering_colleges.to_string(index=False))

# Question 4: Which colleges offer Management?
management_colleges = df.loc[df["Management"] == 1, "College"]
print("\n8) QUESTION 4 - MANAGEMENT COLLEGES")
print(management_colleges.to_string(index=False))

# Question 5: Which colleges offer Law?
law_colleges = df.loc[df["Law"] == 1, "College"]
print("\n9) QUESTION 5 - LAW COLLEGES")
print(law_colleges.to_string(index=False))

# Question 6: Which college covers the most areas?
top_breadth = df.loc[df["Breadth_Score"].idxmax()]
print("\n10) QUESTION 6 - HIGHEST BREADTH")
print(top_breadth["College"], "->", int(top_breadth["Breadth_Score"]), "areas")

# Question 7: Oldest college?
oldest = df.loc[df["Founded_Year"].idxmin()]
print("\n11) QUESTION 7 - OLDEST INSTITUTION")
print(oldest["College"], "->", int(oldest["Founded_Year"]))

# Question 8: Newest college?
newest = df.loc[df["Founded_Year"].idxmax()]
print("\n12) QUESTION 8 - NEWEST INSTITUTION")
print(newest["College"], "->", int(newest["Founded_Year"]))

# Question 9: Average founding year
print("\n13) QUESTION 9 - AVERAGE FOUNDING YEAR")
print(round(df["Founded_Year"].mean(), 2))

# Question 10: Institutions with NIRF 2025 overall data
nirf_available = df.dropna(subset=["NIRF_2025_Overall_Rank"]).sort_values(
    "NIRF_2025_Overall_Rank"
)
print("\n14) QUESTION 10 - NIRF 2025 DATA AVAILABLE IN THIS DATASET")
print(nirf_available[["College", "NIRF_2025_Overall_Rank", "NIRF_2025_Overall_Score"]])

# Question 11: Best NIRF rank among the institutions with published rank
if not nirf_available.empty:
    best_nirf = nirf_available.iloc[0]
    print("\n15) QUESTION 11 - BEST PUBLISHED NIRF 2025 OVERALL RANK")
    print(best_nirf["College"], "->", int(best_nirf["NIRF_2025_Overall_Rank"]))

# Question 12: Highest NIRF score among available entries
nirf_score_available = df.dropna(subset=["NIRF_2025_Overall_Score"]).sort_values(
    "NIRF_2025_Overall_Score", ascending=False
)
print("\n16) QUESTION 12 - HIGHEST PUBLISHED NIRF 2025 OVERALL SCORE")
print(nirf_score_available[["College", "NIRF_2025_Overall_Score"]])

# Question 13: Correlation between founding year and breadth
corr = df["Founded_Year"].corr(df["Breadth_Score"])
print("\n17) QUESTION 13 - CORRELATION: FOUNDING YEAR VS BREADTH")
print(round(corr, 3))

# Question 14: NAAC distribution
naac_counts = df["NAAC_Grade"].value_counts()
print("\n18) QUESTION 14 - NAAC GRADE DISTRIBUTION")
print(naac_counts)

# ---------- 5. Visualizations ----------
plt.rcParams.update({"figure.dpi": 120})

# Graph 1 - Academic breadth
breadth_sorted = df.sort_values("Breadth_Score", ascending=True)

plt.figure(figsize=(11, 6))
plt.barh(breadth_sorted["College"], breadth_sorted["Breadth_Score"])
plt.title("Academic Breadth of Pune Institutions")
plt.xlabel("Number of Broad Academic Areas Represented")
plt.ylabel("Institution")
plt.tight_layout()
plt.savefig(Path(__file__).with_name("01_academic_breadth.png"), dpi=200)
plt.show()
plt.close()

# Graph 2 - Academic area popularity
plt.figure(figsize=(11, 6))
plt.bar(area_counts.index, area_counts.values)
plt.title("Number of Institutions Representing Each Academic Area")
plt.xlabel("Academic Area")
plt.ylabel("Number of Institutions")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(Path(__file__).with_name("02_academic_area_counts.png"), dpi=200)
plt.show()
plt.close()

# Graph 3 - Founding year
founding_sorted = df.sort_values("Founded_Year", ascending=True)

plt.figure(figsize=(11, 6))
plt.barh(founding_sorted["College"], founding_sorted["Founded_Year"])
plt.title("Founding Year Comparison")
plt.xlabel("Year")
plt.ylabel("Institution")
plt.tight_layout()
plt.savefig(Path(__file__).with_name("03_founding_year.png"), dpi=200)
plt.show()
plt.close()

# Graph 4 - NIRF 2025 rank for institutions with rank data
if not nirf_available.empty:
    plot_nirf = nirf_available.sort_values("NIRF_2025_Overall_Rank", ascending=True)

    plt.figure(figsize=(10, 5))
    plt.bar(plot_nirf["College"], plot_nirf["NIRF_2025_Overall_Rank"])
    plt.title("NIRF 2025 Overall Rank (Published Entries Only)")
    plt.xlabel("Institution")
    plt.ylabel("Rank (Lower is Better)")
    plt.xticks(rotation=25, ha="right")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(Path(__file__).with_name("04_nirf_2025_rank.png"), dpi=200)
    plt.show()
    plt.close()

# Graph 5 - Academic-area heatmap using Matplotlib
heatmap_data = df.set_index("College")[area_cols].values

fig, ax = plt.subplots(figsize=(12, 7))
im = ax.imshow(heatmap_data, aspect="auto", interpolation="nearest")

ax.set_xticks(np.arange(len(area_cols)))
ax.set_xticklabels(area_cols, rotation=45, ha="right")
ax.set_yticks(np.arange(len(df)))
ax.set_yticklabels(df["College"])

for i in range(len(df)):
    for j in range(len(area_cols)):
        ax.text(j, i, str(int(heatmap_data[i, j])), ha="center", va="center")

ax.set_title("Academic Area Heatmap")
ax.set_xlabel("Academic Area")
ax.set_ylabel("Institution")
fig.colorbar(im, ax=ax, label="Indicator (1 = represented, 0 = not represented)")
plt.tight_layout()
plt.savefig(Path(__file__).with_name("05_academic_heatmap.png"), dpi=200)
plt.show()
plt.close()

# Graph 6 - NIRF score for published entries only
if not nirf_score_available.empty:
    plot_score = nirf_score_available.sort_values(
        "NIRF_2025_Overall_Score", ascending=True
    )

    plt.figure(figsize=(10, 5))
    plt.barh(plot_score["College"], plot_score["NIRF_2025_Overall_Score"])
    plt.title("NIRF 2025 Overall Score (Published Entries Only)")
    plt.xlabel("NIRF Overall Score")
    plt.ylabel("Institution")
    plt.tight_layout()
    plt.savefig(Path(__file__).with_name("06_nirf_2025_score.png"), dpi=200)
    plt.show()
    plt.close()

# ---------- 6. Derived analysis table ----------
result = df[
    [
        "College", "Founded_Year", "Institution_Type",
        "NAAC_Grade", "NIRF_2025_Overall_Rank",
        "NIRF_2025_Overall_Score", "Breadth_Score"
    ]
].copy()

result["Breadth_Rank"] = (
    result["Breadth_Score"]
    .rank(ascending=False, method="min")
    .astype(int)
)

result = result.sort_values(["Breadth_Rank", "College"])

print("\n19) FINAL DERIVED COMPARISON TABLE")
print(result.to_string(index=False))

# ---------- 7. Export analysis ----------
output = Path(__file__).with_name("pune_colleges_analysis.csv")
result.to_csv(output, index=False)

# ---------- 8. Automatic conclusion ----------
print("\n" + "=" * 80)
print("FINAL CONCLUSION")
print("=" * 80)

print(
    f"\n• {top_breadth['College']} has the highest academic-breadth score "
    f"in this project dataset ({int(top_breadth['Breadth_Score'])} areas)."
)

print(
    f"• {oldest['College']} is the oldest institution in the selected set, "
    f"founded in {int(oldest['Founded_Year'])}."
)

print(
    f"• {newest['College']} is the newest institution in the selected set, "
    f"founded in {int(newest['Founded_Year'])}."
)

if not nirf_available.empty:
    print(
        f"• Among the institutions in this dataset with a published NIRF 2025 "
        f"overall rank, {best_nirf['College']} has the best rank "
        f"({int(best_nirf['NIRF_2025_Overall_Rank'])})."
    )

print(
    "• The NIRF comparison is intentionally limited to institutions for which "
    "a published NIRF 2025 overall rank is present; absence of a rank in this "
    "dataset should NOT be interpreted as 'poor quality'."
)

print(
    "• Breadth_Score is a classroom-derived indicator, not an official ranking."
)

print("\nAnalysis completed successfully.")
