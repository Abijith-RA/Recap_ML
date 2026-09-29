# %%
import pandas as pd
df = pd.read_csv("/home/thinkpad/Documents/BrototypeStudying/Paper two/week 9/data/loan_data.csv")

# %%
print("Shape", df.shape,"\n")
print(df.info(),"\n")

# %%
df.describe().round(2)

# %%
print(df["employment_type"].value_counts(), "\n\n")
print(df["income"].groupby(df["employment_type"]).mean(), "\n\n")
print(df.groupby("employment_type")["default"].mean() * 100)

# %%
import matplotlib.pyplot as plt

plt.boxplot(df["income"].dropna())
plt.ticklabel_format(style="plain", axis="y")

# %% [markdown]
# Here the Dataset Have 605 row of data With on that there the 8 colum have or features 
# age, income, credit_history, loan_amount, default are the numerical column 
# The other two column that string
# Also have outlier and anomalies

# %% [markdown]
# 


