import pandas as pd

data = {
    'Student': ['Amit', 'Neha', 'Raj', 'Pooja'],
    'Mathematics': [75, 92, 80, 88]
}

df = pd.DataFrame(data)

print(df[df["Mathematics"] > 75])