from . import get_program_info

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        
    def get_details(self):
        print(get_program_info())
        return f"Student Name:  {self.name}, Student ID: {self.student_id}"
