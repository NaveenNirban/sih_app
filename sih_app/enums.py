from enum import Enum

class Role(Enum):
    superadmin = 0
    appManager = 1
    admin = 2
    teacher = 3
    student = 4

class CircularFor(Enum):
    everyone = 0
    teachers = 1
    students = 2
    