#package manager - pip (pip install packagename), PyPI  (Python Package Index), Virtualenv 
#popular thrird-party libraries - requests
# scrapy
# Twisted
# Pillow
# lxml
# PyYAML
# Django, Flask, Pyramid
# SQLAlchemy
# numpy, scipy, pandas
# pytest, tox, coverage, mock
# six
# Jinija2
# cryptography
# pylint, flake8, pep8
# pymongo, redis, MySQL-Python, psycopg2

# Additionally, here are a few more libraries that are more specific to a Big Data domain such as:
# RedShift and S3: Amazon services are used with their cloud services. S3 is a storage service and RedShift is a data warehousing service.
# BigQuery: Developed by Google, BigQuery is a Cloud service library that is useful with RESTful APIs.
# PySpark: This is an open-source framework used for large scale data processing and works with resilient distributed datasets.
# Kafka: This is a publish-subscribe messaging system that receives logs in the form of packages and is stored in partitioned spaces.
# Pydoop: Pydoop provides an interface between Hadoop and Python and support for handling its Hadoop distributed file systems.

# TensorFlow: This library was developed by Google in collaboration with the Brain Team. It is an open-source library used for high-level computations. It is also used in machine learning and deep learning algorithms. It contains a large number of tensor operations. Researchers also use this Python library to solve complex computations in Mathematics and Physics.
# Matplotlib: This library is responsible for plotting numerical data. And that’s why it is used in data analysis. It is also an open-source library and plots high-defined figures like pie charts, histograms, scatterplots, graphs, etc.
# Pandas: Pandas are an important library for data scientists. It is an open-source machine learning library that provides flexible high-level data structures and a variety of analysis tools. It eases data analysis, data manipulation, and cleaning of data. Pandas support operations like Sorting, Re-indexing, Iteration, Concatenation, Conversion of data, Visualizations, Aggregations, etc.
# Numpy: The name “Numpy” stands for “Numerical Python”. It is the commonly used library. It is a popular machine learning library that supports large matrices and multi-dimensional data. It consists of in-built mathematical functions for easy computations. Even libraries like TensorFlow use Numpy internally to perform several operations on tensors. Array Interface is one of the key features of this library.
# SciPy: The name “SciPy” stands for “Scientific Python”. It is an open-source library used for high-level scientific computations. This library is built over an extension of Numpy. It works with Numpy to handle complex computations. While Numpy allows sorting and indexing of array data, the numerical data code is stored in SciPy. It is also widely used by application developers and engineers.
# Scrapy: It is an open-source library that is used for extracting data from websites. It provides very fast web crawling and high-level screen scraping. It can also be used for data mining and automated testing of data.
# Scikit-learn: It is a famous Python library to work with complex data. Scikit-learn is an open-source library that supports machine learning. It supports variously supervised and unsupervised algorithms like linear regression, classification, clustering, etc. This library works in association with Numpy and SciPy.
# PyGame: This library provides an easy interface to the Standard Directmedia Library (SDL) platform-independent graphics, audio, and input libraries. It is used for developing video games using computer graphics and audio libraries along with Python programming language.
# PyTorch: PyTorch is the largest machine learning library that optimizes tensor computations. It has rich APIs to perform tensor computations with strong GPU acceleration. It also helps to solve application issues related to neural networks.
# PyBrain: The name “PyBrain” stands for Python Based Reinforcement Learning, Artificial Intelligence, and Neural Networks library. It is an open-source library built for beginners in the field of Machine Learning. It provides fast and easy-to-use algorithms for machine learning tasks. It is so flexible and easily understandable and that’s why is really helpful for developers that are new in research fields.

#Multiple interrelated modules are stored in a library. And whenever we need to use a module, we import it from its library. In Python, it’s a very simple job to do due to its easy syntax. We just need to use import.

# import math
# A = 16
# print(math.sqrt(A))

# from math import sqrt, sin
# A = 16
# B = 3.14
# print(sqrt(A))
# print(sin(B))

#Python modules are reusable pieces of code that can be imported into a program to provide additional functionality.
#Some popular built-in modules include math, datetime, and random, while popular third-party modules include pandas, NumPy, and matplotlib.
#Module is a file that contains code to perform a specific task. A module may contain variables, functions, classes etc. Let's see an example,
#example.py 
# def add(a, b):
#     result = a + b
#     return  result

# import math as m 
# print(m.pi)

# from math import *
# print("The value of  pi is: ", pi)

# calculator.py

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Square root of a negative number is not allowed."

def power(x, y):
    return math.pow(x, y)

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        if choice == '5':  # Square root
            num = float(input("Enter number: "))
            print(f"Square root of {num} is {square_root(num)}")
        elif choice == '6':  # Power
            base = float(input("Enter base number: "))
            exponent = float(input("Enter exponent: "))
            print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()


