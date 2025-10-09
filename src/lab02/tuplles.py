from typing import Tuple

def format_record(rec: Tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Входные данные должны быть кортежем из 3 элементов")
    
    fio, group, gpa = rec
    
    if not isinstance(fio, str) or not isinstance(group, str) or not (isinstance(gpa, float) or isinstance(gpa, int)):
        raise TypeError("Неверные типы элементов записи (fio и group - str, gpa - float или int)")
    
    fio = fio.strip()
    group = group.strip()
    
    if not fio:
        raise ValueError("Пустое ФИО")
    if not group:
        raise ValueError("Пустая группа")
    if not (0 <= gpa <= 5):
        raise ValueError("GPA вне диапазона 0-5")

    parts = fio.split()
    if len(parts) < 2 or len(parts) > 3:
        raise ValueError("ФИО должно содержать 2 или 3 слова")
    
    last_name = parts[0].capitalize()
    initials = ""

    for name in parts[1:]:
        initials += name[0].upper() + "."
    
    return f"{last_name} {initials}, гр. {group}, GPA {gpa:.2f}"


# Тесты
tests = [
    (("Иванов Иван Иванович", "BIVT-25", 4.6), "Иванов И.И., гр. BIVT-25, GPA 4.60"),
    (("Петров Пётр", "IKBO-12", 5.0), "Петров П., гр. IKBO-12, GPA 5.00"),
    (("Петров Пётр Петрович", "IKBO-12", 5.0), "Петров П.П., гр. IKBO-12, GPA 5.00"),
    ((" сидорова анна сергеевна ", "ABB-01", 3.999), "Сидорова А.С., гр. ABB-01, GPA 4.00"),
]

for rec, expected in tests:
    result = format_record(rec)
    print(f"Input: {rec} → Output: {result}")
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"

# Проверка ошибок - несколько примеров:
invalid_tests = [
    ("", "BIVT-25", 4.0),      # пустое ФИО
    ("Иванов Иван", "", 4.0),  # пустая группа
    ("Иванов Иван", "BIVT-25", "4.0"),  # GPA строка вместо числа
    ("Иванов", "BIVT-25", 4.0),          # только фамилия, нет имени
    ("Иванов Иван Иван Иванович", "BIVT-25", 4.0),  # слишком много слов
    ("Иванов Иван", "BIVT-25", 7.0),   # GPA вне диапазона
]

for invalid_rec in invalid_tests:
    try:
        format_record(invalid_rec)
    except (ValueError, TypeError) as e:
        print(f"Input {invalid_rec} вызвало ошибку: {e}")
