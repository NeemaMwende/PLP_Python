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

#example 4
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denomintar: "))
    result = numerator / denominator
    print(f"The result of {numerator} divided by {denominator} is {result}")
except ZeroDivisionError:
    print("Error: cannot divide by zero. Please enter a non-zero denominator.")
except ValueError:
    print("Error: Invalid input. Please enter valid integers")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#example 5
# Define the function g which will raise an IndexError
def g():
    a = "Hello, World!"  # A string of length 13
    index = int(input("Enter an index: "))
    
    # Trying to access an invalid index will raise an IndexError
    print(a[index])
# Define the function f which calls g inside a try block
def f():
    try:
        g()  # Call the function g
    except IndexError:
        # Handle the IndexError raised by g
        print("Please enter a valid index.")
    except ValueError:
        # Handle ValueError in case input is not an integer
        print("Invalid input! Please enter an integer.")
# Call the function f
f()

#example 6
try:
    # Take input from user
    numerator = int(input("Please enter the numerator: "))
    denominator = int(input("Please enter the denominator: "))
    
    # Perform division, which might raise ZeroDivisionError
    result = numerator / denominator
    print(result)

except ZeroDivisionError as e:
    # Accessing specific details of the exception
    print("\n# Type")
    print(type(e))  # Type of the exception

    print("\n# Message")
    print(str(e))  # The default message (uses __str__())

    print("\n# Args")
    print(e.args)  # Arguments that were passed to the exception

#example 7
def check_length(data):
    # Check if the length of data is 5
    if len(data) != 5:
        # Raise a ValueError if the condition is not met
        raise ValueError(f"Expected length 5, but got {len(data)}")
    # If the length is correct, print each element
    for item in data:
        print(item)
# Test the function with a string of length 5
try:
    check_length("hello")  # This will work fine
except ValueError as e:
    print(f"Error: {e}")
# Test the function with a string of length 4 (this will raise an exception)
try:
    check_length("test")  # This will raise the ValueError
except ValueError as e:
    print(f"Error: {e}")
