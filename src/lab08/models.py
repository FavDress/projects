from datetime import datetime, date
from dataclasses import dataclass




@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError("warning: birthdate format might be invalid")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
    
        b = datetime.strptime(self.birthdate, "%Y/%m/%d")
        today = date.today()
        return today.year - b.year

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "gpa": self.gpa,
            "group": self.group
        }

    @classmethod
    def from_dict(cls, d: dict):
        if "fio" not in d.keys():
            raise ValueError("fio is required")
        if "birthdate" not in d.keys():
            raise ValueError("birthdate is required")
        if "group" not in d.keys(): 
            raise ValueError("group is required")
        if "gpa" not in d.keys():
            raise ValueError("gpa is required")
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self):
        return  f"{self.fio}, {self.birthdate}, {self.group}, {self.gpa}"