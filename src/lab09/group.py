import csv
from pathlib import Path
from src.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8") 
        self.rows = []
        self._read_all()

    def _read_all(self):
        with open(self.path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["birthdate"] = row["birthdate"].replace("-", "/")
                row["gpa"] = float(row["gpa"])
                student = Student.from_dict(row)
                self.rows.append(student)

    def list(self):
        return self.rows
    
    def add(self, student: Student):
        self.rows.append(student)


    def find(self, substr: str):
        return [r for r in self.rows if substr in r.to_dict()["fio"]]  
    
    def remove(self, fio: str):
        while True:
            is_found = False
            for i, r in enumerate(self.rows):
                if r.to_dict()["fio"] == fio:
                    self.rows.pop(i)
                    is_found = True
                    break
            if not is_found:
                break

    def update(self, fio: str, **fields):
        student = self.find(fio)[0]
        for key, value in fields.items():
            setattr(student, key, value)

    def __del__(self):
        with open(self.path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=Student.__dataclass_fields__.keys())
            writer.writeheader()
            for student in self.rows:
                writer.writerow(student.to_dict())