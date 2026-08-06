import numpy as np
import matplotlib.pyplot as plt

# Example: speed vs. travel time (classic negative correlation)
speed =       [30, 40, 50, 60, 70, 80]
travel_time = [120, 90, 72, 60, 51, 45]

# Calculate correlation coefficient
r = np.corrcoef(speed, travel_time)[0, 1]
print("Correlation (r):", r)  # Output: something close to -0.97 (strong negative!)

# Visualize it
plt.scatter(speed, travel_time, color='red')
plt.xlabel("Speed (mph)")
plt.ylabel("Travel Time (minutes)")
plt.title(f"Negative Correlation (r = {r:.2f})")
plt.show()
# You'll see points trending DOWN and to the right