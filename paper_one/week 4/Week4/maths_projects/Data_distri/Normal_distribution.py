import numpy as np
import matplotlib.pyplot as plt

# Generate 10,000 random values from a normal distribution
# mean=100, standard deviation=15 (like IQ scores!)
data = np.random.normal(loc=100, scale=15, size=10000)
# loc = mean (center of the bell)
# scale = standard deviation (how spread out)
# size = how many data points to generate

# Plot it as a histogram to SEE the bell shape
plt.hist(data, bins=50, edgecolor='black')
plt.xlabel("IQ Score")
plt.ylabel("Number of People")
plt.title("Normal Distribution of IQ Scores")
plt.show()

# Verify the 68-95-99.7 rule ourselves
# mean = np.mean(data)
# std = np.std(data)

# within_1_std = np.sum((data > mean - std) & (data < mean + std)) / len(data)
# within_2_std = np.sum((data > mean - 2*std) & (data < mean + 2*std)) / len(data)

# print(within_1_std)  # Output: approximately 0.68 (68%)
# print(within_2_std)  # Output: approximately 0.95 (95%)
