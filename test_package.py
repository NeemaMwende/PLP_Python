# test_package.py

# Absolute imports
import mypackage.module1 as m1
import mypackage.module2 as m2

# Using functions from module1
print(m1.greet("Alice"))

# Using functions from module2
print(m2.farewell("Alice"))
print(m2.greet_and_farewell("Alice"))

# test_package_alternative.py

# Import specific functions
# from mypackage.module1 import greet
# from mypackage.module2 import farewell, greet_and_farewell
# print(greet("Bob"))
# print(farewell("Bob"))
# print(greet_and_farewell("Bob"))
