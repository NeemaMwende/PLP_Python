# # astr = 'Hello Bob'
# # try:
# #     istr = int(astr)
# # except:
# #     istr = -1

# # print('First', istr)

# # astr = "123"
# # try:
# #     istr = int(astr)
# # except:
# #     istr = -1

# # print('Second', istr)

# # Prompt the user for two numbers
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     # Attempt to perform division
#     result = num1 / num2

# except ZeroDivisionError:
#     # Handle the case where the user tries to divide by zero
#     print("Error: You cannot divide by zero.")
#     result = None

# except ValueError:
#     # Handle the case where the input is not a valid number
#     print("Error: Invalid input. Please enter a numeric value.")
#     result = None

# else:
#     # If no exceptions occur, this block is executed
#     print("Division successful!")

# finally:
#     # This block is always executed, regardless of an exception
#     if result is not None:
#         print(f"The result of dividing {num1} by {num2} is: {result}")
#     else:
#         print("No valid result to display.")

# Another example
# astr = 'Bob'
# try: 
#     print('Hello')
#     istr = int(astr)
#     print('There')
# except:
#     istr = -1

# print('Done', istr)

# Different example
# rawstr = input('Enter a number:')
# try:
#     ival = int(rawstr)
# except:
#     ival = -1

# if ival > 0:
#     print("Nice work")
# else:
#     print("Not a number")

# # if  x == 5 :
# #     print('Is 5')
# #     print('Is Still 5')
# #     print('Third 5')

# x = 0
# if x < 2 :
#     print('Small')
# elif x < 10 :
#     print('Medium')
# else :
#     print('LARGE')
# print('All done')

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(astr, istr)