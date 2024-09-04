# def thing():
#     print("hello")
#     print("fun")
# thing()
# print("zip")
# thing()

# big = max('Hello world')
# print(big)

# tiny = min("Hello world")
# print(tiny)

# def greet(language):
#     if language == "espaniol":
#         print("Hola")
#     elif language == "french":
#         print("Bonjour")
#     else:
#         print("Hello")

# greet("french")

# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result

# print(factorial(5))  # Output: 120

# def add_nums(a, b):
#     answer = a + b
#     return answer

# total = add_nums(2, 3)
# print(total)

# def add_nums(*nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     return sum
# print("Total: ", add_nums(2, 5, 6, 10, 100, 1000))

# def add_ages(**ages):
#     sum = 0
#     for k, v in ages.items():
#         sum += v
#     return sum
# print("Total: ", add_ages(angel= 23, Lexin=24, Victor=25))

# global_var = 13

# def add_nums(a, b):
#     total = a + b
#     print("Global variable in outer function: ", global_var)
#     def double_it():
#         #local variable
#         double = total * 2
#         print("Global variable in inner function: ", global_var)
#     double_it()
#     return total

# add_nums(13, 5)