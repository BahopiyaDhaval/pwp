import pandas as pd
import numpy as np

# Sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 22],
    'Salary': [50000, 60000, np.nan, 55000]
}

df = pd.DataFrame(data)

print("Before filling missing values:\n", df)

# Fill missing values in 'Age' and 'Salary' with their respective column means
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print("\nAfter filling missing values:\n", df)
