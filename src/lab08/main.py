from src.lab08.models import Student
from src.lab08.serialize import students_from_json, students_to_json

for s in students_from_json("data/samples/student.json"):
    print(s)

students = [
    Student(fio="Иванов Иван Иванович", birthdate="2000/01/15", group="CS-101", gpa=3),
    Student(fio="Петров Петр Петрович", birthdate="1999/11/30", group="CS-102", gpa=3.5),
    Student(fio="Морозова Елена Викторовна", birthdate="2000/03/18", group="CS-102", gpa=2.8),
]

# with open("data/out/students_out.json", "w", encoding="utf-8") as f:
students_to_json(students, "data/out/students_out.json")