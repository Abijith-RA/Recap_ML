import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew

# Let's interpret a real-ish dataset: customer purchase amounts
purchases = [20, 25, 22, 30, 28, 24, 26, 500, 27, 23, 29, 31, 21, 26, 25]

# STEP 1: Look at basic center measures
mean_val = np.mean(purchases)
median_val = np.median(purchases)
print("Mean:", mean_val)      # Output: ~55.1 (dragged up!)
print("Median:", median_val)  # Output: ~26.0 (much lower)

# STEP 2: Check skewness
skew_val = skew(purchases)
print("Skew:", skew_val)  # Output: large positive number -> right-skewed

# STEP 3: Check spread/variability
std_val = np.std(purchases)
print("Std Dev:", std_val)  # Output: large, inflated by that one big value

# STEP 4: Check for outliers using IQR method
Q1 = np.percentile(purchases, 25)
Q3 = np.percentile(purchases, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = [p for p in purchases if p < lower_bound or p > upper_bound]
print("Outliers:", outliers)  # Output: [500]

# STEP 5: Visualize to confirm everything numerically found
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].hist(purchases, bins=10, edgecolor='black')
axs[0].set_title("Histogram")
axs[1].boxplot(purchases)
axs[1].set_title("Boxplot")
plt.show()