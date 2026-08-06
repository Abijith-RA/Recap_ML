import matplotlib.pyplot as plt
import pandas as pd

# A small dataset with MULTIPLE features (like a real ML dataset)
data = pd.DataFrame({
    "size_sqft":     [1000, 1500, 2000, 2500, 3000],
    "num_bedrooms":  [2, 3, 3, 4, 5],
    "age_years":     [20, 15, 10, 5, 2],
    "price":         [200000, 300000, 400000, 500000, 600000]  # our target
})

# Calculate correlation between EVERY pair of columns at once
correlation_matrix = data.corr()

plt.figure(figsize=(6, 5))
plt.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(label="Correlation")
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

# Add the actual numbers as text on top of each cell
for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black')

plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()