import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# --- Import Data ---#
df = pd.read_csv("ab_data.csv")

# --- Data Cleaning & Organization ---#
print(df.isnull().sum())
df = df.drop_duplicates(subset='user_id', keep='first')
print(df["user_id"].duplicated().sum())
mismatch_idx = df[((df['group'] == 'treatment') == (df['landing_page'] == 'old_page'))].index
df.drop(mismatch_idx, inplace=True)

# --- Data Analysis (EDA) ---#
# Descriptive Analysis
print(df.head())
print(df.shape)
print(df.describe())

# Inferential Analysis
# Probability
df['converted'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Total Conversions (0=No, 1=Yes)')
plt.xticks(rotation=0)
# Frequentist
x = df["converted"].value_counts()
A = 254057
B = 34483
S = 288540
P_A = A / (S/100)
P_B = B / (S/100)
print(f"Propability of Buying: {P_B}")
# Bayesian
a = 150
b = 180
samples_a = np.random.beta(1+a, 1+1000-a, 1000)
samples_b = np.random.beta(1+b, 1+1000-b, 1000)
prob_b_better_than_a = (samples_b > samples_a).mean()
print(f"Probability B Better that A: {prob_b_better_than_a}")

# Confidense Intervals
Group_A = df['group'] == 'control'
Conv_a = df.loc[Group_A, 'converted']
Group_B = df['group'] == 'treatment'
Conv_b = df.loc[Group_B, 'converted']
std_a = Conv_a.std()
std_b = Conv_b.std()
margin_error_a = 1.96 * std_a / np.sqrt(len(Conv_a))
margin_error_b = 1.96 * std_b / np.sqrt(len(Conv_b))
Lower_bound_a = Conv_a.mean() - margin_error_a
Upper_bound_a = Conv_a.mean() + margin_error_a
confidence_interval_a = f"[{Lower_bound_a}, {Upper_bound_a}]"
print(f"95% Confidence Interval For Group A: {confidence_interval_a}")
Lower_bound_b = Conv_b.mean() - margin_error_b
Upper_bound_b = Conv_b.mean() + margin_error_b
confidence_interval_b = f"[{Lower_bound_b}, {Upper_bound_b}]"
print(f"95% Confidence Interval For Group B: {confidence_interval_b}")

# Hypothesis Testing
# H0: There is No Difference Between Old and New Buttom
# H1: The New Buttom is Better Than the Old
Group_AB_conv = np.array([Conv_b.sum(), Conv_a.sum()])
nobs = np.array([len(Conv_b), len(Conv_a)])
z_score , P_value = sm.stats.proportions_ztest(Group_AB_conv, nobs, alternative='larger')
if P_value < 0.05:
    # Reject H0
    print("The New Buttom is Better Than the Old")
elif P_value >= 0.05:
    # Reject to Fail H0
    print("There is No Difference Between Old and New Buttom")
