# Using the underscore (_), we can control access to the data inside the Python classes. Python Class has three types of access modifiers:
# Public Access Modifier
# Private Access Modifier
# Protected Access Modifier

class Student:
    schoolName = "PLP Academy"

    def __init__(self, name, age):
        self.name = name
        self.age = age

std = Student("Angel", 25)
std.schoolName
std.age = 30
std.name
print(std.age, std.schoolName, std.name)

#Protected Members
#Protected members of a class are accessible from within the class and are also available to its subclasses. No other environment is permitted access to it. 
class Student:
    _schoolName = "Power Academy"

    def __init__(self, name, age):
        self._name = name
        self._age = age

std = Student("Lexin", 25)
std._schoolName
std._age = 30
std._name
print(std._age, std._schoolName, std._name)

#private members __underscore
class Student:
    __schoolName = "PPP Academy"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __display(self):
        print("THis method is private")

std = Student("Mercy", 25)
std._Student__name
std._Student__age = 30
std._Student__display()
# print(std.__age, std.__schoolName, std.__name)
