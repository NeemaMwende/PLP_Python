#a collection of unique data - cannot be duplicated
student_id = {112, 113, 114, 115, 116, 117, 118, 118}
print('Student Id:', student_id)

# empty_set = set()
# empty_dictionary = { }
# print('Data type of empty set:', type(empty_set)) 
# print('Data type of empty dictionary:', type(empty_dictionary)) 
# student_id.add(120)
# print( student_id)

companies = {'Lacoste', "Ralph Lauren"}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
companies.discard('apple')
print(companies)

fruits = {"Apple", "Peach", "Mango"}
for fruit in fruits:
    print(fruit)

print(len(companies))
print(len(tech_companies))
