#The process of inheriting the properties of the parent class into a child class is called inheritance. The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.
# Single inheritance
# Multiple Inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance

#single inheritance
class Vehicle:
    def Vehicle_info(self):
        print("Inside parent class")
class Car(Vehicle):
    def car_info(self):
        print("INside child class")
car = Car()
car.car_info()
car.Vehicle_info()

#Multiple Inheritance
#Here, a one Child class inherits from multiple parent classes. It means the child class has access to all the parent classes' methods and attributes.
class Person:
    def person_info(self, name, age):
        print("Inside Person class")
        print("Name: ",name, "Age: ",age)

class Company:
    def company_info(self, company_name, location):
        print("Inside Company class")
        print("Name: ",company_name, "Location: ",location)

class Employee(Person, Company, Car):
    def employee_info(self, salary, skill):
        print("Inside Employee class")
        print("Salary: ",salary, "Skill: ",skill)

emp = Employee()
emp.person_info("Jesse", 28)
emp.company_info("Google", "Atlanta")
emp.employee_info(12000, "Machine Learning")

#Multilevel inheritance
# class inherits from a child class or a derived class
class Vehicle:
    def Vehicle_info(self):
        print("Inside grandparent class")

class Car(Vehicle):
    def car_info(self):
        print("Car name is:")

class Sportcar(Car):
    def sportcar_info(self):
        print("Inside sportscar clas")

s_car = Sportcar()
s_car.Vehicle_info()
s_car.car_info()
s_car.sportcar_info()

#hierarchical inheritance - multiple derived child classes from a single parent class
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

# Child class 1 inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def sound(self):
        return "Bark"

# Child class 2 inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the parent class constructor
        self.color = color

    def sound(self):
        return "Meow"

# Creating objects for Dog and Cat classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "White")

# Accessing the methods and attributes
print(f"{dog.name} is a {dog.breed} and it says: {dog.sound()}")
print(f"{cat.name} is a {cat.color} cat and it says: {cat.sound()}")

