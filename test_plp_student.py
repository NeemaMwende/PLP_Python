from plp_student.student import  Student
from plp_student.database  import StudentDatabase

#create  a new student
student1 = Student("Alice", "PLP001")
student2 = Student("Angel",  "PLP002")

#create an instance of studentdatabse and add students
db = StudentDatabase()
db.add_student(student1)
db.add_student(student2)
db.list_students()