# Implicit Conversion - automatic type conversion
# Explicit Conversion - manual type conversion

first_number = 120
second_number = 1.23
new_number = first_number + second_number

print("The new number is", new_number)
print(type(new_number))

# Explicit Conversion - typecasting (user changes)
num_string = "123"
num_integer = 321
print("before typecasting", type(num_string))

num_string = int(num_string)
print("after", num_string, type(num_string))

num_sum = num_integer + num_string
print("sum", num_sum)
print(type(num_sum))

