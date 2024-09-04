#lambda functions - function without a name : Anonymous functions
# snack = lambda : print("Cake")
# snack()

# num_square = lambda num: num ** 2
# print("square is: ", num_square(10))

# def isPalindrome(string):
#     if (string == string[::-1]):
#         return "A Palindrome"
#     else:
#         return "Not a palindrome"

# string = input("Enter string:")
# print(isPalindrome(string))

isPalindrome = lambda string : "Palindrome" if string == string[::-1] else "Not a palindrome"
string = input("Enter a string: ")
print(isPalindrome(string))

# students = [
#     {"name": "Alice", "grade": 85},
#     {"name": "Bob", "grade": 92},
#     {"name": "Charlie", "grade": 87}
# ]

# # Sort by grade
# sorted_students = sorted(students, key=lambda x: x['grade'])
# print(sorted_students)
# # Output: [{'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 87}, {'name': 'Bob', 'grade': 92}]

# # Example with `map()`
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)  # Output: [1, 4, 9, 16, 25]

# # Example with `filter()`
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4]

# numbers = [1, 2, 3, 4, 5]
# doubled = [(lambda x: x * 2)(x) for x in numbers]
# print(doubled)  # Output: [2, 4, 6, 8, 10]
