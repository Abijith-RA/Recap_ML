# %% [markdown]
# ## 1. Dataset Understanding ##

# %%
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")

# %%
df.head(5)

# %%


# %%
df.tail(5)

# %%
row, column = df.shape
print(f"Rows = {row} \nColumns = {column}")

# %%
#for col in df.columns:
#     print(col)
print(list(df.columns))

# %%
print(df.dtypes)

# %%
df.describe().round(2)

# %%
numeric_col = df.select_dtypes(include=["number"]).columns
print("numeric",numeric_col)
category_col = df.select_dtypes(include=["category", "string", "bool"]).columns
print("category", category_col)

# %% [markdown]
# ## 2. Data Quality ##

# %%
df.isnull().sum()

# %%
# percentage = (df.isnull().sum() / df.shape[0]) * 100
percentage = df.isnull().mean() * 100


# %%
print (percentage.round(2))

# %%
df.nunique()

# %%
df.duplicated().value_counts()

# %%
df.columns[df.nunique() < len(df)]

# %%
duplicate_row = df[df.duplicated()]
print(duplicate_row)

# %%
df.groupby("survived")["sex"].value_counts()

# %%
quality_check = pd.DataFrame({
    'type': df.dtypes,
    'missing_%': (df.isnull().mean() * 100).round(1),
    'unique_count': df.nunique()
})
print(quality_check)

# %%
df.groupby("survived")["sex"].value_counts()

# %%
non_use_columns = ["alive", "embark_town", "class", "deck"]
df_use = df.drop(columns=non_use_columns)

# %%
df.corr(numeric_only=True).round(1)

# %%
df.skew(numeric_only=True)

# %%
def uniqueValue(columns):
    print("unique values", df[columns].unique())

uniqueValue("sex")
uniqueValue("embarked")
uniqueValue("pclass")

print("\nAny negative ages?", (df["age"] < 0).any())
print("Any negative fares?", (df["fare"] < 0).any())
print("Any ages > 100?", (df["age"] > 100).any())

print((df["fare"] == 0).sum())

print(df[(df["age"] < 16) & (df["adult_male"] == True)])

# %%
numeric_cols = df.select_dtypes(include=["number"])

Q1 = numeric_cols.quantile(0.25)
Q3 = numeric_cols.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outlier = ((numeric_cols < lower_bound) | (numeric_cols > upper_bound))

outlier_summary = pd.DataFrame({
    "lower bound" : lower_bound.round(2),
    "upper bound" : upper_bound.round(2),
    "outlier count" : outlier.sum(),
    "Outlier %": (outlier.mean() * 100).round(2)
})
print(outlier_summary)

# %%


# %% [markdown]
# ## 3. Univariate Analysis ##

# %%
import matplotlib.pyplot as plt

# %%
print(df["age"].describe())
print(df["age"].skew())
print(df["age"].std() / df["age"].mean())

# %%
clean_age = df["age"].dropna()

plt.hist(clean_age, bins=30, edgecolor = "black")
plt.title("distribution of passenger ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis="y")
plt.show()

# %%
fare_clean = df["fare"].dropna()

plt.hist(fare_clean, bins=40, edgecolor="black")
plt.xlabel("fare")
plt.ylabel("frequency")
plt.title("distribution of passenger fares")

# %%
df["sex"].value_counts()

# %%
df["class"].value_counts()

# %%
df["survived"].value_counts()

# %%
df["embarked"].value_counts(dropna=False)

# %%
count = df["embarked"].fillna("Missing").value_counts()

# %%
plt.bar(count.index, count.values)
plt.show()

# %%
most_common_class = df["pclass"].mode()[0]
print("most common class =", most_common_class)

# %%
most_common_age = df["age"].mode()[0]
print("most common age", most_common_age)

# %% [markdown]
# ## 4. Survival Analysis ##

# %%
sPercentage = round(df["survived"].mean() * 100, 2)

print("survived passenger :", sPercentage)

# %%
nonsPercentage = (df["survived"] == 0).mean()*100
print(nonsPercentage)

# %%
df.groupby("survived")["sex"].value_counts()

# %%
df[df["survived"]==1]["sex"].value_counts()

# %%
df[df["survived"]==1]["pclass"].value_counts()

# %%
df[df["survived"]==1]["embarked"].value_counts()

# %%
df.groupby("age")["survived"].count()

# %%
bins = [0, 12, 18, 35, 60, 100]
labels = ["child", "Teen", "Young Adult", "adult", "Senior"]

df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels, right=True)

# %%
df.groupby("age_group", observed=False)["survived"].mean() * 100

# %%
class_summary = df.groupby("pclass")["survived"].agg(
    Total_passengers="count",
    survivors="sum",
    survive_rate=lambda x: x.mean() * 100
)

# %%
print(class_summary)

# %% [markdown]
# ## 5. Bivariate Analysis ##

# %%
df_corr = df.copy()
df_corr["sex_code"] = df_corr["sex"].map({"female" : 1, "male" : 0})
df_corr["embarked_code"] = df_corr["embarked"].map({"S" : 1, "C" : 2, "Q" : 3})

cols = ["survived", "pclass", "sex_code", "age", "fare", "embarked_code"]
matrix = df_corr[cols].corr()

# %%
plt.Figure(figsize=(8, 6))

sns.heatmap(matrix, annot=True, cmap="coolwarm")
plt.title("Correlation heatmap with survived")

# %%
fare_summary = df.groupby("pclass")["fare"].agg(
        mean = "mean",
        median = "median",
        min = "min",
        max = "max",
        std = "std"
    ).round(2)

# %%
print(fare_summary)

# %%
age_passenger_summary = df.groupby("pclass")["age"].agg(
    
    mean = "mean",
    median = "median",
    min = "min",
    max = "max",
    std = "std"
).round(2)
print(age_passenger_summary)

# %%
sns.regplot(x="sibsp", y="survived", data=df, logistic=True)
plt.show()

# %%
df["parch"].corr(df["survived"])

# %% [markdown]
# ## 6. Multivariate Analysis ##

# %%
survival_plot_S_Pc = df.pivot_table(values="survived", index="pclass", columns="sex", aggfunc="mean")
print(survival_plot_S_Pc)

# %%
sns.barplot(x="pclass", y="survived", hue="sex", data=df,edgecolor = "black")
plt.show()

# %%
survival_plot_s_p_a = df.pivot_table(values="survived", index=["pclass", "age"], columns="sex", aggfunc="mean")
print(survival_plot_s_p_a)

# %%
bins = [0, 12, 18, 60, 100]
labels = ["Child", "Teen", "Adult", "Senior"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
print(df["age_group"])

# %%
sns.catplot(
    x="pclass",
    y="survived",
    hue="sex",
    col="age_group",
    data=df,
    kind="bar",
)
plt.show()

# %%
features = ["age", "fare", "sibsp", "survived"]
sns.pairplot(df[features], hue="survived", palette="coolwarm")
plt.show()

# %%
port_class_pivot = df.pivot_table(
    values="survived", index="pclass", columns="embarked", aggfunc="mean"
)

print(port_class_pivot)

# %%
port_age_pivot = df.pivot_table(
    values="survived", index="age_group", columns="sex", aggfunc="mean"
)
print(port_age_pivot)

# %%
df["sibsp"].value_counts()

# %%
plot_family_count = df.pivot_table(
    values="survived", index="sibsp", columns="sex", aggfunc="mean"
)
print(plot_family_count)

# %%
df.groupby(["sex", "pclass", "age_group"])["survived"].mean().sort_values(ascending=False)
