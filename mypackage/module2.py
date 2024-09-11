# module2.py
from .module1 import greet  # Relative import

def farewell(name):
    return f"Goodbye, {name} from module2!"

def greet_and_farewell(name):
    greeting = greet(name)  # Calling the function from module1
    farewell_message = farewell(name)
    return f"{greeting} {farewell_message}"
