#Errors detected during execution are called exceptions and are not unconditionally fatal.
#IdexError, KeyError, NameError, TypeERror, ZeroDivisionError

try: 
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
else:
    print("The rsult is", result)
finally:
    print("Execution completed")

#example 2
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: the file was not found")
except IOError:
    print("Error: an IOError occured")
else:
    print("File content:", content)
finally:
    print("File handling operation completed")

#example 3
# Dictionary of students with their ages
students = {"Nora": 15, "Gino": 30}
# Prompt user for input
name = input("Please enter the name of the student: ")
try:
    # Try to get the age of the student
    age = students[name]
    print(f"The age of {name} is {age}.")
except KeyError:
    # Handle the case where the name is not in the dictionary
    print(f"Error: Student with name '{name}' not found.")
