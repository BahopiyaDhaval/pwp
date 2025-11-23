import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'Salary': [70000.0, 50000.0, 60000.0],
    'IsManager': [True, False, True]
}

df = pd.DataFrame(data)

# Check data types of each column
print(df.dtypes)
