from .student import Student

class StudentDatabase:
    def  __init__(self):
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        print(f"Added {student.name} to the database.")
        
    def list_students(self):
        print("Listing all  students:")
        for student in self.students:
            print(student.get_details())