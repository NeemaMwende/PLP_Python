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

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(5))  # Output: 120
