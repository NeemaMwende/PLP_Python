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
        

