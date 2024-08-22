num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))

# list
languages = ['python', 'java', 'c++']
print(languages)
print(languages[1])

#tuple - immutable (cannot be changed after creating)
product = ('apple', 'mango', 3000)
print(product[0])

#set - unordered and unindexed
fruits = {'apple', 'mango', 'banana'}
print(fruits)
print(type(fruits))

#dictionary - key value pairs (ordered collection)
capital_city = {"Nepal":"Kathmandu", "India":"Delhi"}
print(capital_city)
print(capital_city["Nepal"])