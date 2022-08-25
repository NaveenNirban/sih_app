from enum import Enum

class Role:
    Admin = "ORGANIZATION"
    HOD = "HOD"
    Teacher = "TEACHER"
    Student = "STUDENT"
    Parent = "PARENT"

class CircularFor(Enum):
    everyone = 0
    teachers = 1
    students = 2
    