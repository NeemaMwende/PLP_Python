# Question One: large_power function

def large_power(base, exponent):
    result = base ** exponent

    if result > 5000:
        return True
    else:
        return False

# Get user input
base = float(input("Enter base number: "))
exponent = float(input("Enter exponent number: "))

# Call the function with the user-provided inputs
print("Is the result greater than 5000?", large_power(base, exponent))

# Question Two: divisible_by_ten function

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# Get user input
num = int(input("Enter a number: "))

# Call the function with the user-provided input
print("Is the number divisible by 10?", divisible_by_ten(num))
