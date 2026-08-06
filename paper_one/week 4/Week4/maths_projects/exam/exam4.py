import pandas as pd

data = {
    "Marks": [65, 70, 75, 80, 80, 85, 90]
}

df = pd.DataFrame(data)

average = df.mean()
middle = df.median()
frequency = df.mode()


print(average)
print(middle)
print(frequency)

