# E-commerce Conversion Optimization — A/B Testing Analysis

> A statistical pipeline for evaluating landing page button performance using Frequentist and Bayesian inference across 288,540 user sessions.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![scipy](https://img.shields.io/badge/scipy-statistical%20testing-8CAAE6?style=flat&logo=scipy&logoColor=white)
![statsmodels](https://img.shields.io/badge/statsmodels-z--test-4B8BBE?style=flat)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)

---

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Usage](#usage)
- [Pipeline](#pipeline)
- [Hypothesis Testing](#hypothesis-testing)
- [Sample Output](#sample-output)
- [Notes](#notes)

---

## Overview

This project analyzes an A/B test comparing two versions of an e-commerce landing page button — the **original (control)** vs. a **redesigned version (treatment)** — to determine whether the new button drives a statistically significant improvement in conversions.

The analysis covers the full pipeline:

1. **Data cleaning** — deduplication and mismatch removal
2. **Exploratory analysis** — descriptive stats and conversion distribution
3. **Frequentist probability** — raw conversion rates per group
4. **Bayesian simulation** — Beta posterior sampling to estimate P(B > A)
5. **Confidence intervals** — 95% CI for each group's conversion rate
6. **Hypothesis testing** — one-sided Z-test for proportions at α = 0.05

---

## Dataset

Place `ab_data.csv` in the same directory as the script. The file should contain the following columns:

| Column | Type | Values | Description |
|---|---|---|---|
| `user_id` | `int` | unique | Unique identifier per user session |
| `group` | `str` | `control` · `treatment` | Experiment arm assignment |
| `landing_page` | `str` | `old_page` · `new_page` | Page variant shown to the user |
| `converted` | `int` | `0` · `1` | Whether the user completed a purchase |

---

## Requirements

Install all dependencies with:

```bash
pip install pandas numpy scipy statsmodels matplotlib seaborn
```

```
pandas
numpy
scipy
statsmodels
matplotlib
seaborn
```

---

## Usage

```bash
python "E-commerce_Conversion_Optimization_A_Statistical_AB_Testing_Analysis.py"
```

> Make sure `ab_data.csv` is in the same working directory before running.

---

## Pipeline

### 1 · Data Cleaning

- Removes rows with null values
- Deduplicates on `user_id`, keeping the first occurrence
- Drops mismatched rows where group assignment and landing page don't align (e.g. a `treatment` user seeing the `old_page`)

### 2 · Exploratory Data Analysis

- Prints `head()`, `shape()`, and `describe()` for a quick data overview
- Bar chart of overall conversion distribution (converted vs. not converted)

### 3 · Frequentist Probability

Calculates raw conversion rates for both groups directly from observed counts.

### 4 · Bayesian Analysis

Simulates posterior distributions using a **Beta distribution** and estimates the probability that the treatment group outperforms control:

```
P(B > A) via Monte Carlo sampling over 1,000 draws
Priors: α = 150, β = 180
```

### 5 · Confidence Intervals

Computes **95% confidence intervals** for the conversion rate of each group:

```
CI = mean ± 1.96 × (std / √n)
```

### 6 · Hypothesis Testing

A one-sided **Z-test for proportions** (`statsmodels.stats.proportions_ztest`) tests whether the treatment group converts at a meaningfully higher rate than control.

---

## Hypothesis Testing

| | |
|---|---|
| **H₀** | There is no difference between the old and new button conversion rates |
| **H₁** | The new button achieves a higher conversion rate than the original |
| **Test** | One-sided proportions Z-test |
| **Significance level** | α = 0.05 |
| **Decision rule** | Reject H₀ if p-value < 0.05 |

---

## Sample Output

```
Probability of Buying (Group B):         11.95%
P(B converts better than A) — Bayesian:  ~0.87
95% CI — Control   (Group A):            [0.1173, 0.1192]
95% CI — Treatment (Group B):            [0.1170, 0.1189]

Result: There is no significant difference between old and new button.
```

---

## Notes

**Bayesian priors** — The simulation uses `α = 150`, `β = 180` as priors over 1,000 Beta samples. Adjust these values in the script to reflect different prior beliefs about expected baseline conversion rates.

**One-sided test** — The Z-test uses `alternative='larger'`, testing specifically whether treatment out-converts control — not simply that the two groups differ.

**Mismatch removal** — Rows where group and landing page are inconsistent are dropped before analysis to preserve the integrity of the experiment.

**Deduplication** — Only the first record per `user_id` is kept. This prevents repeat visitors from inflating conversion counts in either group.

---

## Project Structure

```
.
├── ab_data.csv                                                               # Input dataset (not included)
└── E-commerce_Conversion_Optimization_A_Statistical_AB_Testing_Analysis.py   # Main analysis script
└── E-commerce Presentation.pptx                                              # Presentation Findings
└── README.md
```
