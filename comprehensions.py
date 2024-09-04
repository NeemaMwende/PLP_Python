# nums = [4, -11, 69, 53, -65]
# doubled = []

# for num in nums:
#     doubled.append(num * 2)

# print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]

squares = [x**2 for x in range(10)]
print(squares)

square_dict = {x: x**2 for x in range(10)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(square_dict)

unique_squares = {x**2 for x in range(10)}
# Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
print(unique_squares)

square_gen = (x**2 for x in range(10))
for square in square_gen:
    print(square)

