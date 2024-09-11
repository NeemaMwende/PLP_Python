#It provides data structures and functions for working with structured data, such as tables of numerical and textual data. Pandas is built on top of the NumPy library, which provides efficient array operations in Python.
#It is particularly useful for data analysis, data manipulation, and data visualization tasks.
#Pandas provides two main data structures: Series and DataFrame. A Series is a one-dimensional array-like object that can hold any data type. It has an associated index, which labels each element in the Series. A DataFrame is a two-dimensional table-like structure that contains rows and columns of data. It is similar to a spreadsheet or a SQL table. Each column in a DataFrame is a Series.
#Pandas provides a wide range of functions for reading and writing data to and from various file formats, including CSV, Excel, SQL databases, and more. It also provides functions for data cleaning, filtering, sorting, merging, and grouping.


# Here are some examples of what you can do with Pandas:
# Load data from a CSV file into a DataFrame
# Filter and sort data in a DataFrame based on certain criteria
# Compute summary statistics of the data, such as mean, median, and standard deviation
# Aggregate data using group-by operations
# Visualize data using built-in plotting functions

# import pandas as pd
# data =  {'Name': ['John', 'Anna', 'Peter', 'Linda'],
#          'Age': [28, 24, 35, 32],
#          'Country': ['USA', 'UK', 'Australia', 'Germany']}
# df = pd.DataFrame(data)
# print(df['Name'])
# print(df[['Name', 'Age']])
# print(df.loc[0])
# print(df[df['Age'] > 30])

# df['Salary'] = [50000, 80000, 90000, 10000]
# print(df)

# grouped = df.groupby('Age')['Salary'].mean()
# print(grouped)


# import  pandas as pd
# cs = pd.read_csv('my_file.txt')
# print(cs)

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('text.txt')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Calculate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Filter students who scored above 85 in Math
high_math_scorers = df[df['Math Score'] > 85]
print("\nStudents with Math Score above 85:")
print(high_math_scorers)

# Calculate the average scores by Grade
average_scores_by_grade = df.groupby('Grade').mean()
print("\nAverage Scores by Grade:")
print(average_scores_by_grade[['Math Score', 'English Score', 'Science Score']])

# Plot the average Math Scores by Grade
plt.figure(figsize=(10, 6))
average_scores_by_grade['Math Score'].plot(kind='bar', color='skyblue')
plt.title('Average Math Scores by Grade')
plt.xlabel('Grade')
plt.ylabel('Average Math Score')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()
