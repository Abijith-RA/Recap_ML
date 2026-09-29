# %%
import pandas as pd

df = pd.read_csv("/home/thinkpad/Documents/BrototypeStudying/Paper two/week 8/code/data/raw_employee_data.csv")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df.info()

# %%
df = df.dropna(subset="salary")

# %%
df.isnull().sum()

# %%
df = df.drop(columns=["employee_id", "name", "email", "phone", "gender", "education", "join_date", "notes","performance_rating"])

# %%
df.isnull().sum()

# %%
from sklearn.model_selection import train_test_split

x = df.drop(columns=["salary"])
y = df["salary"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# %%
x_train.info()
x_train.isnull().sum()

# %%
import matplotlib.pyplot as plt

x_train.boxplot()
plt.show()

# %%
# median_age = df["age"].median()
# df.loc[df["age"] > 100 , "age"] = median_age
# df.loc[df["age"] > 100, "age"]

# %%
median_age = x_train["age"].median()

# %%
Q1 = x_train["age"].quantile(0.25)
Q3 = x_train["age"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outlier = x_train[(df["age"] < lower_bound) | (df["age"] > upper_bound)]

print(outlier)

# %%
x_train.dtypes

# %%
x_train.loc[x_train["age"] > 100, "age"] = median_age

# %%
x_test.loc[x_test["age"] > 100, "age"] = median_age

# %%
x_train["age"].dtype
x_test["age"].dtype

# %%
x_train["age"] = x_train["age"].fillna(x_train["age"].median())
x_test["age"] = x_test["age"].fillna(x_train["age"].median())

# %%
x_train.isnull().sum()
# x_test.isnull().sum()

# %%
department_mode = x_train["department"].mode()[0]

# %%
x_train["department"] = x_train["department"].fillna(department_mode)
x_test["department"] = x_test["department"].fillna(department_mode)

# %%
x_train.isnull().sum()
# x_test.isnull().sum()

# %%
x_train["city"].mode()[0]

# %%
x_train["city"] = x_train["city"].fillna(x_train["city"].mode()[0])
x_test["city"] = x_test["city"].fillna(x_train["city"].mode()[0])

# %%


# %%
Q1 = df["years_experience"].quantile(0.25)
Q3 = df["years_experience"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outlier = df[(df["years_experience"] < lower_bound )|(df["years_experience"] > upper_bound )]
print(lower_bound,upper_bound)
print(outlier)

# %%
# #Check every row - is years_experience impossible for that person's age?
# invalid_age = df["years_experience"] > (df["age"] - 18)

# #For only the broken rows, fix years_experience = age - 18 (never below 0)
# df.loc[invalid_age, "years_experience"] = (df.loc[invalid_age, "age"] - 18).clip(lower=0)

# df.loc[df["years_experience"] > 60, "years_experience"] = df["years_experience"].median()
# df.loc[df["years_experience"] < 0, "years_experience"] = df["years_experience"].median()

# %%
result = pd.merge(x_train, y_train, left_index=True,right_index=True,how="inner")
print(result.head(5))

# %%
x_train["years_experience"] = x_train["years_experience"].fillna(x_train["years_experience"].median())
x_test["years_experience"] = x_test["years_experience"].fillna(x_train["years_experience"].median())

# %%
x_train.isnull().sum()
x_test.isnull().sum()

# %%
mode_remoteWork = x_train["remote_work"].mode()[0]
x_train["remote_work"] = x_train["remote_work"].fillna(mode_remoteWork)
x_test["remote_work"] = x_test["remote_work"].fillna(mode_remoteWork)

# %%
invalid_value = x_train["years_experience"] > (x_train["age"] - 18)
x_train.loc[invalid_value, "years_experience"] = (x_train.loc[invalid_value, "age"] - 18).clip(lower=0)

in_test_invalid_value = x_test["years_experience"] > (x_test["age"] - 18)
x_test.loc[in_test_invalid_value, "years_experience"] = (x_test.loc[in_test_invalid_value, "age"] - 18).clip(lower=0)


# %%
# def remove_expOutliers(dataset,column):
#     dataset.loc[dataset[column] > 60,"age"] = dataset[column].median()
#     return dataset

# remove_expOutliers(x_train,"age")

# %%
x_train.loc[df["age"] < 18 ,"age"] = x_train["age"].median()

# %%
# x_train.groupby("age").size()

# %%
x_train[x_train["years_experience"] > 15]

# %%
x_train.boxplot()
plt.show()

# %%
x_train["remote_work"].value_counts().plot(kind="bar")
plt.show()

# %%
y_train.info()

# %%
y_train = y_train.astype(str).str.replace(r'[^\d.]',"",regex = True).astype(float)
y_train = y_train.astype(int)
print(y_train.dtype)
y_test = y_test.astype(str).str.replace(r'[^\d.]',"",regex = True).astype(float).astype(int)


# %%
y_train.groupby(x_train["remote_work"]).mean()

# %%
x_train["department"].unique()

# %%
x_train["department"] = x_train["department"].str.strip().str.lower()

# %%
dept_map = {
    "suport" : "support",
    "i.t." : "it",
    "human resources" : "hr",
    "h.r." : "hr",
    "markting" : "marketing",
    "ops" : "operations"
}

x_train["department"] = x_train["department"].replace(dept_map)

# %%
x_train["city"].unique()

# %%
x_train["city"] = x_train["city"].str.strip().str.lower()

# %%
city_map = {
    "nyc" : "new york"
}

x_train["city"] = x_train["city"].replace(city_map)

# %%
x_train["city"].value_counts()

# %%
x_test["department"].unique()

# %%
x_test["department"] = x_test["department"].str.strip().str.lower()
x_test["department"] = x_test["department"].replace(dept_map)

# %%
x_test["city"].unique()

# %%
x_test["city"] = x_test["city"].str.strip().str.lower()
x_test["city"] = x_test["city"].replace(city_map)

# %%
x_train = pd.get_dummies(x_train, columns=["department", "city"], drop_first=True).astype(int)
x_test = pd.get_dummies(x_test, columns=["department", "city"], drop_first=True).astype(int)

# %%
y_train.describe().round(2)

# %%
y_train = y_train.astype(float).astype(int)

# %%
y_train[y_train > 200000] = y_train.median().astype(int)

# %%
y_test[y_test > 200000] = y_train.median()

# %%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

cols_to_scale = ["age", "years_experience"]

x_train[cols_to_scale] = scaler.fit_transform(x_train[cols_to_scale])
x_test[cols_to_scale] = scaler.transform(x_test[cols_to_scale])


# %%
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train,y_train)

pred = model.predict(x_test)

# %%
from sklearn.metrics import mean_absolute_error,r2_score

print("MAE :", mean_absolute_error(y_test,pred))

print("R2 :", r2_score(y_test,pred))

# %%
# from sklearn.ensemble import RandomForestRegressor

# model = RandomForestRegressor(n_estimators=200, random_state=42)
# model.fit(x_train, y_train)
# preds = model.predict(x_test)

# print("MAE:", mean_absolute_error(y_test, preds))
# print("R²:", r2_score(y_test, preds))

# %%
# importances = pd.Series(model.feature_importances_, index=x_train.columns).sort_values(ascending=False)
# print(importances)

# %%
# x_train = x_train.drop(columns=[c for c in x_train.columns if c.startswith("city_")])
# x_test = x_test.drop(columns=[c for c in x_test.columns if c.startswith("city_")])


