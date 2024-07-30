# import numpy as np
# from scipy import stats

# # Sample data for three groups
# group1 = np.array([5, 7, 8])
# group2 = np.array([6, 6, 8])
# group3 = np.array([7, 8, 9])

# # Perform one-way ANOVA
# f_statistic, p_value = stats.f_oneway(group1, group2, group3)

# print("One-Way ANOVA Test Results:")
# print(f"F-Statistic: {f_statistic}")
# print(f"P-Value: {p_value}")

# # Interpret the result
# alpha = 0.05  # Significance level
# if p_value < alpha:
#     print("Reject the null hypothesis: There are significant differences between the group means.")
# else:
#     print("Fail to reject the null hypothesis: No significant differences between the group means.")

# #####################################################################

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols #pip install statsmodels


# Sample data
data = {
    'Method': ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B'],
    'Class': ['Online', 'Online', 'Online', 'In-person', 'In-person', 'In-person',
              'Online', 'Online', 'Online', 'In-person', 'In-person', 'In-person'],
    'Score': [85, 88, 90, 92, 95, 91, 75, 78, 80, 88, 85, 87]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Perform Two-Way ANOVA
model = ols('Score ~ C(Method) * C(Class)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("Two-Way ANOVA Test Results:")
print(anova_table)

# Interpretation
alpha = 0.05  # Significance level
if anova_table['PR(>F)']['C(Method)'] < alpha:
    print("Method effect is significant.")
else:
    print("Method effect is not significant.")

if anova_table['PR(>F)']['C(Class)'] < alpha:
    print("Class effect is significant.")
else:
    print("Class effect is not significant.")

if anova_table['PR(>F)']['C(Method):C(Class)'] < alpha:
    print("Interaction effect is significant.")
else:
    print("Interaction effect is not significant.")
