# E-Commerce A/B Testing: Call to Action Optimization

## Project Overview
An e-commerce company wants to optimize its website by changing the "Call to Action" (CTA) button from the old design to a new one (e.g., from "Buy Now" to "Add to Cart"). This project evaluates the results of an A/B test to determine if the new button statistically improves the user conversion rate.

Users were divided into two groups:
**Control Group (A):** Users who interacted with the old CTA button.
**Treatment Group (B):** Users who interacted with the new CTA button.

## Dataset & Cleaning
- **Original Data:** User interaction logs containing group assignments and conversion status (0 = No, 1 = Yes).
- **Data Cleaning:** Removed duplicate `user_id` entries and filtered out mismatched records (e.g., control users seeing the treatment page).
- **Final Sample Size:** ~288,540 unique users.

## Statistical Methodology
This analysis goes beyond simple conversion rates, utilizing a robust statistical pipeline:

### 1. Probability & Distributions
**Bernoulli/Binomial Distribution:** Modeled each user's click as a binary outcome (Success/Failure).
* Calculated the baseline probability of conversion for both groups.

### 2. Confidence Intervals
* Constructed **95% Confidence Intervals** for the conversion rates of each group.
* Analyzed the overlap between intervals to visually assess potential significance.

### 3. Frequentist Hypothesis Testing
**Null Hypothesis (H0):** There is no difference in conversion rates between the old and new buttons.
**Alternative Hypothesis (H1):** The new button yields a higher conversion rate.
**Method:** Conducted a Z-test for proportions to calculate the p-value.

### 4. Bayesian Inference
* Simulated 10,000 samples using the **Beta Distribution** to calculate the exact posterior probability that Treatment (B) is better than Control (A).

## Results & Business Conclusion
* The Z-test yielded a p-value significantly higher than the 0.05 threshold. **We fail to reject the null hypothesis.**
* The Power Analysis confirmed a statistical power of ~100%, meaning the test was highly sensitive. The lack of statistical significance is due to a genuine lack of difference, not a lack of data.

---
*Disclaimer: The statistical analysis, data cleaning, and core Python code were independently developed. Generative AI tools were used solely to assist with proofreading and structuring this Markdown presentation.*
