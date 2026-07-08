import pandas as pd

df = pd.read_csv("08-07-2026_data.csv")

# head()- Returns the first 5 rows of the DataFrame
print(df.head())

# tail() - Returns the last 5 rows of the DataFrame
print(df.tail())

# info() - Displays summary information about the DataFrame.
print(df.info())

# describe() - Generates statistical summary of numerical columns.
print(df.describe())

# columns - Returns the names of all columns in the DataFrame.
print(df.columns)

# shape - Returns the number of rows and columns as a tuple.
print(df.shape)

# sort_values() - Sorts the DataFrame by the specified column.
print(df.sort_values("Marks"))

# loc - Accesses rows and columns using labels.
print(df.loc[0])

# iloc - Accesses rows and columns using integer positions.
print(df.iloc[1])

# mean() - Calculates the average value of a numerical column.
print(df["Marks"].mean())
