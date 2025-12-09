from src.lab09.group import Group
from src.lab08.models import Student

g = Group("data/samples/students.csv")
g.add(Student(fio="John Doe", birthdate="2000/01/01", gpa=3.5, group="SE-01"))
g.remove("John Doe")
g.update("Морозова Елена", gpa=3.9)