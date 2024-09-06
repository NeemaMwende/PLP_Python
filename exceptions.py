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