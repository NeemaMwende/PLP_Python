#simpliest form is by the print statement
# def add(a, b):
#     result = a + b
#     print(f"The result is {result}")
#     return result
# result = add(2, 3)
# print(f"The final result is {result}")

#using pdb, python's interactive source code debugger : n for next, c for continue, q for quit
import pdb;

def add_numbers(a, b):
    pdb.set_trace()
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(f"sum: {sum_result}")