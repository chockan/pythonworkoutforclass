import numpy as np
from scipy.stats import chi2_contingency

# Contingency Table: Gender vs. Product Preference
# Format: [ [Male, Female], [Product A, Product B] ]
observed = np.array([[30, 20],  # Product A
                     [25, 25]])  # Product B

# Perform Chi-Square Test
chi2_stat, p_value, dof, expected = chi2_contingency(observed)

print("Chi-Square Test of Independence:")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies:\n{expected}")
