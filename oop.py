# Building blocks of OOP
# Classes - a blueprint of an object
# Objects - an instance of a class
# Methods - methods represent behaviors
# Attributes - information to be stored in a class about an object

# Inheritance: child classes inherit data and behaviors from the parent class
# Encapsulation: containing information in an object, exposing only selected information
# Abstraction: only exposing high-level public methods for accessing an object
# Polymorphism: many methods can do the same task

#class attributes
# class Person:
#     name = 'Angel'
# Person.name

# details = Person()
# details.name

# instance attributes
# class Person:
#     nationality = 'Kenyan'
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.birthday = ""        
# p1 = Person()
# p1.name = "Angel"
# p1.age = 60
# p1.birthday = "November"
# print(p1.name)
# print(p1.age)
# print(p1.birthday)

# class Friend:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age
# p2 = Friend("Angel", "female", 90)
# p2.name = "Lexin"
# p2.gender = "Male"
# p2.age = 60
# print(p2.name, p2.gender, p2.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayInfo(self):
        print("Person Name: ", self.name, "Age: ",self.age)

p1 = Person("Victor", 20)
p1.displayInfo()