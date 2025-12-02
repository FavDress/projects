import json
from src.lab08.models import Student

def students_to_json(students: list[Student], path: str):
    data = []
    for elm in students:
        data.append(elm.to_dict())

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> list[Student]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)


    result = []
    for elm in data:
        try:
            student = Student.from_dict(elm)
            result.append(student)
        except ValueError:
            continue

        
    return result