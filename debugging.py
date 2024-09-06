#simpliest form is by the print statement
# def add(a, b):
#     result = a + b
#     print(f"The result is {result}")
#     return result
# result = add(2, 3)
# print(f"The final result is {result}")

#using pdb, python's interactive source code debugger : n for next, c for continue, q for quit
# import pdb;
# def add_numbers(a, b):
#     pdb.set_trace()
#     result = a + b
#     return result
# sum_result = add_numbers(5, 3)
# print(f"sum: {sum_result}")

#breakpoint debugger : By default, breakpoint() will import pdb and call pdb.set_trace()
# PYTHONBREAKPOINT=0
# def multiply(a, b):
#     breakpoint()
#     result = a * b
#     return result
# product = multiply(5, 3)
# print(f"Product: {product}")

#python -m pdb my_script.py (another way is to use this in the terminal instead of breakpoint and pdb's)
filename = __file__
import pdb; pdb.set_trace()
print(f"path = {filename}")