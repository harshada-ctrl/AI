# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:48:44 2026

@author: Admin
"""

# ============================================================
# REAL-LIFE STATISTICS PROJECT
# STUDENT LIFESTYLE, LEARNING HABITS & DOMAIN SKILL DEVELOPMENT
# COMPLETE STATISTICAL ANALYSIS
# ============================================================

# ============================================================
# LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t


# ============================================================
# 1. READ DATA
# ============================================================

file_path = "C:\8-statistics\Student Lifestyle, Learning Habits & Domain Skill Development Analyticsd final clean dataset 1.csv"

df = pd.read_csv(file_path)

print("\n" + "=" * 60)
print("DATA UNDERSTANDING")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())


# ============================================================
# 2. REMOVE EMPTY COLUMNS
# ============================================================

df = df.dropna(axis=1, how="all")

print("\nShape after removing empty columns:")
print(df.shape)


# ============================================================
# 3. DATA INFORMATION
# ============================================================

print("\n" + "=" * 60)
print("DATA INFORMATION")
print("=" * 60)

print("\nData types and information:")
print(df.info())

print("\nDescriptive overview:")
print(df.describe(include="all"))


# ============================================================
# 4. MISSING VALUES AND DUPLICATES
# ============================================================

print("\n" + "=" * 60)
print("DATA CLEANING CHECK")
print("=" * 60)

print("\nMissing values by column:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())

print("\nDuplicate records:")
print(df.duplicated().sum())


# ============================================================
# 5. RENAME IMPORTANT COLUMNS
# ============================================================

df = df.rename(columns={

    "1. Student Age": "Age",

    "2. Gender": "Gender",

    "3. Engineering Branch": "Branch",

    "4. Year of Study": "Year",

    "5. Which domain do you want to build your career in?":
        "Domain",

    "6. How clear are you about your chosen career domain?":
        "Career_Clarity",

    "7. How many hours do you sleep per day?":
        "Sleep",

    "8. How many hours per day do you spend on mobile phones for non-academic purposes?":
        "Mobile",

    "9. How many hours per day do you spend on entertainment/social media/gaming?":
        "Entertainment",

    "10. How many hours per day do you spend on self-learning?":
        "Self_Learning",

    "11. How many hours per week do you spend developing your career-domain skills?":
        "Domain_Practice",

    "12. How many hours per week do you spend on physical activity/sports/walking?":
        "Physical_Activity",

    "13. How many hours per week do you spend working on practical projects?":
        "Project_Hours",

    "14. How would you rate your current skill level in your chosen domain?":
        "Domain_Skill",

    "15. How many domain-specific projects have you completed?":
        "Projects",

    "16. How many of these projects were developed independently by you?":
        "Independent_Projects",

    "17. How frequently do you practice your domain skills?":
        "Practice_Frequency",

    "18. How many hours per week do you spend solving real-world/domain-specific problems?":
        "Problem_Solving_Hours",

    "19. How many domain-related courses/certifications have you completed?":
        "Courses",

    "20. How many internships or industry projects have you completed?":
        "Internships",

    "21. How confident are you in applying your domain knowledge to a real-world problem?":
        "Real_World_Confidence",

    "22. If you receive a new problem in your chosen domain, how confident are you that you can solve it independently?":
        "Problem_Confidence",

    "23. How confident are you in explaining your project to an industry professional?":
        "Project_Confidence",

    "24. How confident are you about getting an internship/job in your chosen domain?":
        "Career_Confidence"
})


print("\nRenamed columns:")
print(df.columns.tolist())


# ============================================================
# 6. CHECK NUMERICAL COLUMNS
# ============================================================

numerical_columns = [

    "Age",
    "Career_Clarity",
    "Sleep",
    "Mobile",
    "Entertainment",
    "Self_Learning",
    "Domain_Practice",
    "Physical_Activity",
    "Project_Hours",
    "Domain_Skill",
    "Projects",
    "Independent_Projects",
    "Problem_Solving_Hours",
    "Courses",
    "Internships",
    "Real_World_Confidence",
    "Problem_Confidence",
    "Project_Confidence",
    "Career_Confidence"
]

for column in numerical_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# 7. INVALID VALUE CHECK
# ============================================================

print("\n" + "=" * 60)
print("INVALID VALUE CHECK")
print("=" * 60)

# Age

if "Age" in df.columns:

    invalid_age = df[
        (df["Age"] < 15) |
        (df["Age"] > 100)
    ]

    print("\nInvalid age records:")
    print(len(invalid_age))


# Skill rating

if "Domain_Skill" in df.columns:

    invalid_skill = df[
        (df["Domain_Skill"] < 1) |
        (df["Domain_Skill"] > 5)
    ]

    print("\nInvalid domain skill records:")
    print(len(invalid_skill))


# Career confidence

if "Career_Confidence" in df.columns:

    invalid_confidence = df[
        (df["Career_Confidence"] < 1) |
        (df["Career_Confidence"] > 5)
    ]

    print("\nInvalid career confidence records:")
    print(len(invalid_confidence))


# Sleep

if "Sleep" in df.columns:

    invalid_sleep = df[
        (df["Sleep"] < 0) |
        (df["Sleep"] > 24)
    ]

    print("\nInvalid sleep records:")
    print(len(invalid_sleep))


# ============================================================
# 8. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

variables = [

    "Self_Learning",
    "Domain_Practice",
    "Project_Hours",
    "Entertainment",
    "Sleep",
    "Projects",
    "Domain_Skill",
    "Career_Confidence"
]

statistics_results = []

for column in variables:

    data = df[column].dropna().to_numpy()

    if len(data) == 0:
        continue

    print("\n" + "-" * 50)
    print("Variable:", column)

    mean = np.mean(data)
    median = np.median(data)

    values, counts = np.unique(
        data,
        return_counts=True
    )

    mode = values[np.argmax(counts)]

    minimum = np.min(data)
    maximum = np.max(data)

    range_value = maximum - minimum

    variance = np.var(
        data,
        ddof=1
    )

    standard_deviation = np.std(
        data,
        ddof=1
    )

    q1 = np.percentile(
        data,
        25
    )

    q3 = np.percentile(
        data,
        75
    )

    iqr = q3 - q1

    percentile_90 = np.percentile(
        data,
        90
    )

    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Mode:", mode)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Range:", round(range_value, 2))
    print("Variance:", round(variance, 2))
    print("Standard Deviation:", round(standard_deviation, 2))
    print("Q1:", round(q1, 2))
    print("Q3:", round(q3, 2))
    print("IQR:", round(iqr, 2))
    print("90th Percentile:", round(percentile_90, 2))

    statistics_results.append({

        "Variable": column,
        "Mean": round(mean, 2),
        "Median": round(median, 2),
        "Mode": mode,
        "Minimum": minimum,
        "Maximum": maximum,
        "Range": round(range_value, 2),
        "Variance": round(variance, 2),
        "Standard Deviation": round(standard_deviation, 2),
        "Q1": round(q1, 2),
        "Q3": round(q3, 2),
        "IQR": round(iqr, 2),
        "90th Percentile": round(percentile_90, 2)

    })


statistics_table = pd.DataFrame(
    statistics_results
)

print("\n\nSTATISTICAL SUMMARY TABLE")
print(statistics_table)


# ============================================================
# 9. CORRELATION ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("CORRELATION ANALYSIS")
print("=" * 60)

correlations = [

    ("Self_Learning", "Domain_Skill"),

    ("Domain_Practice", "Domain_Skill"),

    ("Projects", "Domain_Skill"),

    ("Entertainment", "Self_Learning"),

    ("Domain_Skill", "Career_Confidence"),

    ("Projects", "Career_Confidence")

]

correlation_results = []

for x, y in correlations:

    temp = df[
        [x, y]
    ].dropna()

    if len(temp) < 2:

        print(
            x,
            "vs",
            y,
            "= Not enough data"
        )

        continue

    correlation = np.corrcoef(
        temp[x],
        temp[y]
    )[0, 1]

    print(
        x,
        "vs",
        y,
        "=",
        round(correlation, 3)
    )

    correlation_results.append({

        "Variable 1": x,
        "Variable 2": y,
        "Correlation": round(
            correlation,
            3
        )

    })


correlation_table = pd.DataFrame(
    correlation_results
)

print("\nCorrelation Summary:")
print(correlation_table)


# ============================================================
# 10. 95% CONFIDENCE INTERVAL
# ============================================================

print("\n" + "=" * 60)
print("95% CONFIDENCE INTERVAL")
print("=" * 60)


def confidence_interval(column):

    data = df[column].dropna().to_numpy()

    n = len(data)

    if n < 2:

        print(
            "\nNot enough data for:",
            column
        )

        return None

    mean = np.mean(data)

    std = np.std(
        data,
        ddof=1
    )

    standard_error = (
        std /
        np.sqrt(n)
    )

    t_value = t.ppf(
        0.975,
        n - 1
    )

    margin_error = (
        t_value *
        standard_error
    )

    lower = mean - margin_error

    upper = mean + margin_error

    print("\nVariable:", column)
    print("Sample Size:", n)
    print("Sample Mean:", round(mean, 2))

    print(
        "95% Confidence Interval:",
        round(lower, 2),
        "to",
        round(upper, 2)
    )

    return mean, lower, upper


domain_practice_ci = confidence_interval(
    "Domain_Practice"
)

domain_skill_ci = confidence_interval(
    "Domain_Skill"
)


# ============================================================
# 11. DOMAIN-WISE ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("DOMAIN-WISE ANALYSIS")
print("=" * 60)

domain_analysis = df.groupby(
    "Domain"
).agg(

    Students=(
        "Domain_Skill",
        "count"
    ),

    Average_Skill=(
        "Domain_Skill",
        "mean"
    ),

    Average_Practice_Hours=(
        "Domain_Practice",
        "mean"
    )

)

domain_analysis[
    "Average_Skill"
] = domain_analysis[
    "Average_Skill"
].round(2)

domain_analysis[
    "Average_Practice_Hours"
] = domain_analysis[
    "Average_Practice_Hours"
].round(2)


print(domain_analysis)


# ============================================================
# 12. CATEGORY COUNTS
# ============================================================

print("\n" + "=" * 60)
print("CATEGORY COUNTS")
print("=" * 60)

print("\nGender:")
print(df["Gender"].value_counts())

print("\nBranch:")
print(df["Branch"].value_counts())

print("\nYear:")
print(df["Year"].value_counts())

print("\nCareer Domain:")
print(df["Domain"].value_counts())


# ============================================================
# 13. SAMPLE SIZE CHECK
# ============================================================

print("\n" + "=" * 60)
print("SAMPLE SIZE CHECK")
print("=" * 60)

sample_size = len(df)

print(
    "Current sample size:",
    sample_size
)

required_sizes = [
    30,
    50,
    100,
    150
]

sample_results = []

for size in required_sizes:

    if sample_size >= size:

        sample = df.sample(
            n=size,
            random_state=42
        )

        mean_value = np.mean(
            sample["Domain_Practice"]
        )

        print(
            "Sample size:",
            size,
            "Sample mean:",
            round(mean_value, 2)
        )

        sample_results.append({

            "Sample Size": size,
            "Sample Mean": round(
                mean_value,
                2
            )

        })

    else:

        print(
            "Sample size:",
            size,
            "Cannot be taken from current dataset."
        )


sample_result = pd.DataFrame(
    sample_results
)


# ============================================================
# 14. MEMBER 3 — MATPLOTLIB VISUALIZATION
# ============================================================

print("\n" + "=" * 60)
print("MEMBER 3 — VISUALIZATION")
print("=" * 60)


# ------------------------------------------------------------
# 14.1 SELF-LEARNING HISTOGRAM
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Self_Learning"].dropna(),
    bins=8,
    edgecolor="black"
)

plt.title(
    "Distribution of Self-Learning Hours"
)

plt.xlabel(
    "Self-Learning Hours per Day"
)

plt.ylabel(
    "Number of Students"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 14.2 DOMAIN PRACTICE HISTOGRAM
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Domain_Practice"].dropna(),
    bins=8,
    edgecolor="black"
)

plt.title(
    "Distribution of Weekly Domain Practice Hours"
)

plt.xlabel(
    "Domain Practice Hours per Week"
)

plt.ylabel(
    "Number of Students"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 14.3 ENTERTAINMENT HISTOGRAM
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Entertainment"].dropna(),
    bins=8,
    edgecolor="black"
)

plt.title(
    "Distribution of Entertainment Hours"
)

plt.xlabel(
    "Entertainment Hours per Day"
)

plt.ylabel(
    "Number of Students"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 14.4 SLEEP HISTOGRAM
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Sleep"].dropna(),
    bins=8,
    edgecolor="black"
)

plt.title(
    "Distribution of Daily Sleep Hours"
)

plt.xlabel(
    "Sleep Hours per Day"
)

plt.ylabel(
    "Number of Students"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 14.5 PROJECT EXPERIENCE HISTOGRAM
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Projects"].dropna(),
    bins=8,
    edgecolor="black"
)

plt.title(
    "Distribution of Completed Domain Projects"
)

plt.xlabel(
    "Number of Projects"
)

plt.ylabel(
    "Number of Students"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 14.6 DOMAIN SKILL BOXPLOT
# ------------------------------------------------------------

plt.figure(figsize=(7, 5))

plt.boxplot(
    df["Domain_Skill"].dropna()
)

plt.title(
    "Boxplot of Domain Skill Rating"
)

plt.ylabel(
    "Domain Skill Rating"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ============================================================
# 15. CATEGORICAL VISUALIZATION
# ============================================================


# ------------------------------------------------------------
# 15.1 CAREER DOMAIN DISTRIBUTION
# ------------------------------------------------------------

domain_counts = df[
    "Domain"
].value_counts()

plt.figure(figsize=(10, 6))

plt.bar(
    domain_counts.index,
    domain_counts.values
)

plt.title(
    "Career Domain Distribution"
)

plt.xlabel(
    "Career Domain"
)

plt.ylabel(
    "Number of Students"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 15.2 BRANCH-WISE DISTRIBUTION
# ------------------------------------------------------------

branch_counts = df[
    "Branch"
].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    branch_counts.index,
    branch_counts.values
)

plt.title(
    "Branch-Wise Student Distribution"
)

plt.xlabel(
    "Engineering Branch"
)

plt.ylabel(
    "Number of Students"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 15.3 YEAR-WISE DISTRIBUTION
# ------------------------------------------------------------

year_counts = df[
    "Year"
].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    year_counts.index,
    year_counts.values
)

plt.title(
    "Year-Wise Student Distribution"
)

plt.xlabel(
    "Year of Study"
)

plt.ylabel(
    "Number of Students"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 15.4 SKILL LEVEL DISTRIBUTION
# ------------------------------------------------------------

skill_counts = df[
    "Domain_Skill"
].value_counts().sort_index()

plt.figure(figsize=(8, 5))

plt.bar(
    skill_counts.index.astype(str),
    skill_counts.values
)

plt.title(
    "Domain Skill Level Distribution"
)

plt.xlabel(
    "Skill Rating"
)

plt.ylabel(
    "Number of Students"
)

plt.xticks(
    [str(i) for i in range(1, 6)],
    [
        "1 - Beginner",
        "2 - Basic",
        "3 - Intermediate",
        "4 - Advanced",
        "5 - Highly Skilled"
    ],
    rotation=20
)

plt.tight_layout()
plt.show()


# ============================================================
# 16. BIVARIATE ANALYSIS
# ============================================================


# ------------------------------------------------------------
# 16.1 SELF-LEARNING VS DOMAIN SKILL
# ------------------------------------------------------------

temp = df[
    [
        "Self_Learning",
        "Domain_Skill"
    ]
].dropna()

correlation = np.corrcoef(
    temp["Self_Learning"],
    temp["Domain_Skill"]
)[0, 1]

plt.figure(figsize=(8, 5))

plt.scatter(
    temp["Self_Learning"],
    temp["Domain_Skill"]
)

plt.title(
    "Self-Learning Hours vs Domain Skill\n"
    f"Correlation = {correlation:.3f}"
)

plt.xlabel(
    "Self-Learning Hours per Day"
)

plt.ylabel(
    "Domain Skill Rating"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 16.2 DOMAIN PRACTICE VS DOMAIN SKILL
# ------------------------------------------------------------

temp = df[
    [
        "Domain_Practice",
        "Domain_Skill"
    ]
].dropna()

correlation = np.corrcoef(
    temp["Domain_Practice"],
    temp["Domain_Skill"]
)[0, 1]

plt.figure(figsize=(8, 5))

plt.scatter(
    temp["Domain_Practice"],
    temp["Domain_Skill"]
)

plt.title(
    "Domain Practice Hours vs Domain Skill\n"
    f"Correlation = {correlation:.3f}"
)

plt.xlabel(
    "Domain Practice Hours per Week"
)

plt.ylabel(
    "Domain Skill Rating"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 16.3 PROJECTS VS DOMAIN SKILL
# ------------------------------------------------------------

temp = df[
    [
        "Projects",
        "Domain_Skill"
    ]
].dropna()

correlation = np.corrcoef(
    temp["Projects"],
    temp["Domain_Skill"]
)[0, 1]

plt.figure(figsize=(8, 5))

plt.scatter(
    temp["Projects"],
    temp["Domain_Skill"]
)

plt.title(
    "Number of Projects vs Domain Skill\n"
    f"Correlation = {correlation:.3f}"
)

plt.xlabel(
    "Number of Completed Projects"
)

plt.ylabel(
    "Domain Skill Rating"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 16.4 ENTERTAINMENT VS SELF-LEARNING
# ------------------------------------------------------------

temp = df[
    [
        "Entertainment",
        "Self_Learning"
    ]
].dropna()

correlation = np.corrcoef(
    temp["Entertainment"],
    temp["Self_Learning"]
)[0, 1]

plt.figure(figsize=(8, 5))

plt.scatter(
    temp["Entertainment"],
    temp["Self_Learning"]
)

plt.title(
    "Entertainment Hours vs Self-Learning Hours\n"
    f"Correlation = {correlation:.3f}"
)

plt.xlabel(
    "Entertainment Hours per Day"
)

plt.ylabel(
    "Self-Learning Hours per Day"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 16.5 DOMAIN SKILL VS CAREER CONFIDENCE
# ------------------------------------------------------------

temp = df[
    [
        "Domain_Skill",
        "Career_Confidence"
    ]
].dropna()

correlation = np.corrcoef(
    temp["Domain_Skill"],
    temp["Career_Confidence"]
)[0, 1]

plt.figure(figsize=(8, 5))

plt.scatter(
    temp["Domain_Skill"],
    temp["Career_Confidence"]
)

plt.title(
    "Domain Skill vs Career Confidence\n"
    f"Correlation = {correlation:.3f}"
)

plt.xlabel(
    "Domain Skill Rating"
)

plt.ylabel(
    "Career Confidence Rating"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 16.6 PROJECTS VS CAREER CONFIDENCE
# ------------------------------------------------------------

temp = df[
    [
        "Projects",
        "Career_Confidence"
    ]
].dropna()

correlation = np.corrcoef(
    temp["Projects"],
    temp["Career_Confidence"]
)[0, 1]

plt.figure(figsize=(8, 5))

plt.scatter(
    temp["Projects"],
    temp["Career_Confidence"]
)

plt.title(
    "Number of Projects vs Career Confidence\n"
    f"Correlation = {correlation:.3f}"
)

plt.xlabel(
    "Number of Completed Projects"
)

plt.ylabel(
    "Career Confidence Rating"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ============================================================
# 17. CONFIDENCE INTERVAL VISUALIZATION
# ============================================================

print("\n" + "=" * 60)
print("CONFIDENCE INTERVAL VISUALIZATION")
print("=" * 60)


def get_confidence_interval(column):

    data = df[
        column
    ].dropna().to_numpy()

    n = len(data)

    if n < 2:
        return None

    mean = np.mean(data)

    std = np.std(
        data,
        ddof=1
    )

    standard_error = (
        std /
        np.sqrt(n)
    )

    t_value = t.ppf(
        0.975,
        n - 1
    )

    margin_error = (
        t_value *
        standard_error
    )

    lower = mean - margin_error

    upper = mean + margin_error

    return mean, lower, upper


dp_result = get_confidence_interval(
    "Domain_Practice"
)

ds_result = get_confidence_interval(
    "Domain_Skill"
)


if dp_result is not None and ds_result is not None:

    means = [
        dp_result[0],
        ds_result[0]
    ]

    lower_errors = [
        dp_result[0] - dp_result[1],
        ds_result[0] - ds_result[1]
    ]

    upper_errors = [
        dp_result[2] - dp_result[0],
        ds_result[2] - ds_result[0]
    ]

    plt.figure(figsize=(8, 5))

    plt.errorbar(

        [
            "Domain Practice",
            "Domain Skill"
        ],

        means,

        yerr=[
            lower_errors,
            upper_errors
        ],

        fmt="o",

        capsize=6

    )

    plt.title(
        "95% Confidence Intervals"
    )

    plt.ylabel(
        "Mean Value"
    )

    plt.grid(
        axis="y",
        alpha=0.3
    )

    plt.tight_layout()
    plt.show()


# ============================================================
# 18. SAMPLE SIZE VS SAMPLE MEAN
# ============================================================

print("\n" + "=" * 60)
print("SAMPLE SIZE VS SAMPLE MEAN")
print("=" * 60)

sample_sizes = [
    30,
    50,
    100,
    150
]

sample_means = []

for size in sample_sizes:

    if len(df) >= size:

        sample = df.sample(
            n=size,
            random_state=42
        )

        mean_value = np.mean(
            sample["Domain_Practice"]
        )

        sample_means.append(
            mean_value
        )

    else:

        sample_means.append(
            np.nan
        )


sample_result = pd.DataFrame({

    "Sample Size":
        sample_sizes,

    "Sample Mean":
        sample_means

})


print(sample_result)


plt.figure(figsize=(8, 5))

plt.plot(

    sample_result["Sample Size"],

    sample_result["Sample Mean"],

    marker="o"

)

plt.title(
    "Sample Size vs Sample Mean"
)

plt.xlabel(
    "Sample Size"
)

plt.ylabel(
    "Mean Weekly Domain Practice Hours"
)

plt.grid(
    alpha=0.3
)

plt.tight_layout()
plt.show()


# ============================================================
# 19. DOMAIN-WISE VISUALIZATION
# ============================================================


# ------------------------------------------------------------
# 19.1 AVERAGE SKILL BY DOMAIN
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(

    domain_analysis.index,

    domain_analysis[
        "Average_Skill"
    ]

)

plt.title(
    "Average Domain Skill by Career Domain"
)

plt.xlabel(
    "Career Domain"
)

plt.ylabel(
    "Average Domain Skill"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 19.2 AVERAGE PRACTICE HOURS BY DOMAIN
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(

    domain_analysis.index,

    domain_analysis[
        "Average_Practice_Hours"
    ]

)

plt.title(
    "Average Domain Practice Hours by Career Domain"
)

plt.xlabel(
    "Career Domain"
)

plt.ylabel(
    "Average Practice Hours per Week"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()
plt.show()


# ============================================================
# 20. DAILY TIME ALLOCATION
# ============================================================

print("\n" + "=" * 60)
print("DAILY TIME ALLOCATION")
print("=" * 60)

average_sleep = np.mean(
    df["Sleep"].dropna()
)

average_entertainment = np.mean(
    df["Entertainment"].dropna()
)

average_self_learning = np.mean(
    df["Self_Learning"].dropna()
)

average_domain_practice_daily = (
    np.mean(
        df["Domain_Practice"].dropna()
    ) / 7
)


activities = [

    "Sleep",

    "Entertainment",

    "Self-Learning",

    "Domain Practice"

]


hours = [

    average_sleep,

    average_entertainment,

    average_self_learning,

    average_domain_practice_daily

]


time_table = pd.DataFrame({

    "Activity": activities,

    "Average Hours Per Day": np.round(
        hours,
        2
    )

})


print(time_table)


plt.figure(figsize=(9, 5))

plt.bar(

    activities,

    hours

)

plt.title(
    "Average Daily Time Allocation"
)

plt.xlabel(
    "Activity"
)

plt.ylabel(
    "Average Hours per Day"
)

plt.xticks(
    rotation=20
)

plt.tight_layout()
plt.show()


# ============================================================
# 21. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL PROJECT SUMMARY")
print("=" * 60)

print(
    "\nTotal number of students:",
    len(df)
)

print(
    "Total number of variables:",
    len(df.columns)
)

print(
    "\nRequired minimum sample size:",
    30
)

if len(df) >= 30:

    print(
        "Sample size status: SUFFICIENT"
    )

else:

    print(
        "Sample size status: "
        "CURRENTLY BELOW REQUIRED MINIMUM"
    )

    print(
        "Additional responses needed:",
        30 - len(df)
    )


print(
    "\nAnalysis includes:"
)

print(
    "✓ Pandas data reading and cleaning"
)

print(
    "✓ Data understanding"
)

print(
    "✓ Missing-value analysis"
)

print(
    "✓ Duplicate analysis"
)

print(
    "✓ Invalid-value checks"
)

print(
    "✓ Descriptive statistics"
)

print(
    "✓ Correlation analysis"
)

print(
    "✓ 95% confidence intervals"
)

print(
    "✓ Domain-wise analysis"
)

print(
    "✓ Histograms"
)

print(
    "✓ Boxplot"
)

print(
    "✓ Categorical bar charts"
)

print(
    "✓ Scatter plots"
)

print(
    "✓ Confidence interval visualization"
)

print(
    "✓ Sample size experiment"
)

print(
    "✓ Daily time allocation"
)

print(
    "✓ Domain-wise visualizations"
)

print(
    "\n========== ANALYSIS COMPLETED =========="
)