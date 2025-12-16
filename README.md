LAB01
1.
```python
name = input('Имя:')
age = int(input('Возраст:'))
next_age = age + 1
print(f'Привет, {name}! Через год тебе будет {next_age}.')
```
2.
```python
a = input('a:')
b = input('b:')

x = float(a.replace(',','.'))
y = float(b.replace(',','.'))

sum1 = x+y
avg1 = round((x+y)/2, 2)
print(f'sum={sum1}; avg={avg1}')
```
3.
```python
price = float(input('Цена(₽):'))
discount = float(input('Скидка(%):'))
vat = float(input('НДС(%):'))

base = price * (1-discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

base_r = round(base, 2)
vat_r = round(vat_amount, 2)
total_r = round(total, 2)

print("База после скидки:", base_r, "₽")
print("НДС:              ", vat_r, "₽")
print("Итого к оплате:   ", total_r, "₽")
```
4.
```python
m = int(input('Минуты:'))
h = m//60
mn = m%60
if mn < 10:
    print(f'{h}:0{mn}')
else:
    print(f'{h}:{mn}')
```
5.
```python
st = str(input()) 
ini = '' 
while '  ' in st: 
    st = st.replace('  ', ' ') 
st = st.strip() 
for a in st: 
    if a.isupper(): 
        ini += a 
 
 
print(ini) 
print(len(st))
```


LAB02
1.
![cod1](./images/Lab02.Задание%201%20код.png)
![min_max](./images/Lab02.Задание%201%20тесты%20для%20min_max.png)
![unique_sorted](./images/Lab02.Задание%201%20тесты%20для%20unique_sorted.png)
![flatten](./images/Lab02.Задание%201%20тесты%20для%20flatten.png)
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError('Список пуст')
    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique = set(nums)
    return sorted(unique)


def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError('строка не строка строк матрицы')
        for elem in row:
            result.append(elem)
    return result

# Тесты для min_max
print(min_max([3, -1, 5, 5, 0]))         
print(min_max([42]))                        
print(min_max([-5, -2, -9]))                
try:
    print(min_max([]))                      
except ValueError as e:
    print(e)
print(min_max([1.5, 2, 2.0, -3.1]))        

# Тесты для unique_sorted
print(unique_sorted([3, 1, 2, 1, 3]))       
print(unique_sorted([]))                    
print(unique_sorted([-1, -1, 0, 2, 2]))     
print(unique_sorted([1.0, 1, 2.5, 2.5, 0])) 

# Тесты для flatten
print(flatten([[1, 2], [3, 4]]))               
print(flatten([[1, 2], (3, 4, 5)]))            
print(flatten([[1], [], [2, 3]]))               
try:
    print(flatten([[1, 2], "ab"]))             
except TypeError as e:
    print(e) 
```
2.
![cod2](./images/Lab02.Задание%202%20код.png)
![transpose](./images/Lab02.Задание%202%20тесты%20transpose.png)
![row_sums](./images/Lab02.Задание%202%20row_sums.png)
![col_sums](./images/Lab02.Задание%202%20col_sums.png)
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("рваная матрица")
    return [[mat[row_idx][col_idx] for row_idx in range(len(mat))] for col_idx in range(row_length)]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("рваная матрица")
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("рваная матрица")
    return [sum(mat[row_idx][col_idx] for row_idx in range(len(mat))) for col_idx in range(row_length)]


# Тесты

# transpose
print(transpose([[1, 2, 3]]))            
print(transpose([[1], [2], [3]]))         
print(transpose([[1, 2], [3, 4]]))        
print(transpose([]))                       
try:
    print(transpose([[1, 2], [3]]))        
except ValueError as e:
    print(e)

# row_sums
print(row_sums([[1, 2, 3], [4, 5, 6]]))   
print(row_sums([[-1, 1], [10, -10]]))      
print(row_sums([[0, 0], [0, 0]]))          
try:
    print(row_sums([[1, 2], [3]]))          
except ValueError as e:
    print(e)

# col_sums
print(col_sums([[1, 2, 3], [4, 5, 6]]))   
print(col_sums([[-1, 1], [10, -10]]))      
print(col_sums([[0, 0], [0, 0]]))         
try:
    print(col_sums([[1, 2], [3]]))          
except ValueError as e:
    print(e)
```
3.
![cod3](./images/Lab02.Задание%203%20код.png)
![tests](./images/Lab02.Задание%203%20тесты.png)
![mistakes](./images/Lab02.Задание%203%20проверка%20ошибок.png)
```python
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

```
______________________________________________________________________________________________________________________________________
LAB03


```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", 'е').replace("Ё", "Е")

    text = text.replace("\n", ' ').replace("\r", " ").replace("\t", " ")

    result = text.split()
    result = " ".join(result)

    return result



def tokenize(text: str) -> list[str]:
    pattern = r"\w+(?:-\w+)*"
    pattern = re.compile(pattern)
    result = re.findall(pattern, text)

    return result



def count_freq(tokens: list[str]) -> dict[str, int]:
    stats = {}

    for word in tokens:
        stats[word] = stats.get(word, 0) + 1

    return stats




def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freq = list(freq.items())
    freq.sort(key=lambda x: (-x[1], x[0]))
    return freq[:n]
```




```python
from text import normalize, top_n, count_freq, tokenize


def test_normalize():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка", yo2e=True) == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize( "  двойные   пробелы  ") == "двойные пробелы"

def test_top_n():
    assert top_n({"a":3,"b":2,"c":1}, n=2) == [("a",3), ("b",2)]
    assert top_n({"aa":2,"bb":2,"cc":1}, n=2) == [("aa",2), ("bb",2)]


def test_count_freq():
    assert count_freq(["a","b","a","c","b","a"]) =={"a": 3, "b": 2, "c": 1}
    assert count_freq(["bb","aa","bb","aa","cc"]) == {"aa": 2, "bb": 2, "cc": 1}

def test_tokenize():
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

def main():
    test_normalize()
    test_top_n()
    test_count_freq()
    test_tokenize()

if __name__ == "__main__":
    main()
```





```python
from  lib.text  import count_freq, top_n, normalize, tokenize

data = input()
data_normalized = normalize(data)
tokens = tokenize(data_normalized)
stats = count_freq(tokens)
top = top_n(stats)
print(f"Всего слов: {len(tokens)}\nУникальных слов: {len(stats)}\nТоп-5:")
for elm in top:
    print(f"{elm[0]}:{elm[1]}")
```
![text_stats](/images/Lab03.%20Text_stats.png)
__________________________________________________________________________________________________________________________________
LAB04

```python
from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as file:
        res = file.read().replace("\n", " ")

    return res


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if len(rows) > 0:
        for elm in rows:
            if len(rows[0]) != len(elm):
                raise ValueError

    with open(path, "w", newline="", encoding="utf-8") as file:
        wr = csv.writer(file, delimiter=",")
        if header is not None:
            wr.writerow(header)
        wr.writerows(rows)
```




```python
from lib.text import count_freq, top_n, normalize, tokenize
from lab04.io_txt_csv import read_text, write_csv

data = read_text("lab04/data/input.txt")
data_normalized = normalize(data)
tokens = tokenize(data_normalized)
stats = count_freq(tokens)
top = top_n(stats)


rows = list(stats.items())
rows.sort(key=lambda x: (-x[1], x[0]))

write_csv(rows, "lab04/data/report.csv", header=("word","count"))

print(f"Всего слов: {len(tokens)}\nУникальных слов: {len(stats)}\nТоп-5:")
for elm in top:
    print(f"{elm[0]}:{elm[1]}")
```
![text_report](/images/Lab04.text_report.не%20пустой%20файл.png)
![text_report](/images/Lab04.text_report.пустой%20файл.png)

______________________________________________________________________________________________________________________________________________________________________
LAB05

```python
import json
import csv
from pathlib import Path





def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    if (Path(json_path).suffix != ".json"):
        raise ValueError("Input file must be a JSON file")

    if (Path(csv_path).suffix != ".csv"):
        raise ValueError("Output file must be a CSV file")
    
    if Path(json_path).exists() is False:
        raise FileNotFoundError("File not found")

    with open(json_path, "r", encoding="utf-8") as iFile:
        json_data = json.load(iFile)
    
    if len(json_data) == 0:
        raise ValueError("Input JSON file is empty")

    
    fieldnames = json_data[0].keys()
    with open(csv_path, "w", newline="", encoding="utf-8") as oFile:
        wr = csv.DictWriter(oFile, fieldnames=fieldnames, delimiter=",")
        wr.writeheader()
        wr.writerows(json_data)

    




def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    if (Path(json_path).suffix != ".json"):
        raise ValueError("Input file must be a JSON file")

    if (Path(csv_path).suffix != ".csv"):
        raise ValueError("Output file must be a CSV file")
    
    if Path(csv_path).exists() is False:
        raise FileNotFoundError("File not found")


    json_data = []
    with open(csv_path, "r", encoding="utf-8") as iFile:
        rd = csv.DictReader(iFile)
        for row in rd:
            json_data.append(row)
    
    if len(json_data) == 0:
        raise ValueError("Input CSV file is empty")

    with open(json_path, "w", encoding="utf-8") as oFile:
        json.dump(json_data, oFile, ensure_ascii=False, indent=2)
```



```python
from openpyxl import Workbook
import csv
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """

    if (Path(xlsx_path).suffix != ".xlsx"):
        raise ValueError("Input file must be a XLSX file")

    if (Path(csv_path).suffix != ".csv"):
        raise ValueError("Output file must be a CSV file")
    
    if Path(csv_path).exists() is False:
        raise FileNotFoundError("File not found")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    data = []
    with open(csv_path, "r", encoding="utf-8") as iFile:
        rd = csv.reader(iFile)
        for row in rd:
            data.append(row)

    if len(data) == 0:
        wb.save(xlsx_path)
        raise ValueError("Input CSV file is empty")

    for row in data:
        ws.append(row)

    for col in ws.columns:
        length = max(len(str(cell.value)) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max(length, 8)
    
    wb.save(xlsx_path)
```

SAMPLES:
![SAMPLES.CITIESCSV](/images/Lab05.samples.citiesCSV.png)
![SAMPLES.PEOPLECSV](/images/Lab05.peopleCSV.png)
![SAMPLES.PEOPLEJSON](/images/Lab05.peopleJSON.png)

OUT:
![OUTLL](/images/Lab05LL.png)
![OUTJSON](/images/Lab05JSON.png)
![OUTCH](/images/Lab05CH.png)
____________________________________________________________________________________________________________________________________________________________________________
LAB06
```python
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def add_command_parsers(com_parser):
    com_parser.add_argument("--input", required=True, type=str, help="Путь к входному файлу")
    com_parser.add_argument("--output", required=True, type=str, help="Путь к выходному файлу")


parser = argparse.ArgumentParser(description="CLI для конвертации файлов")
subparsers = parser.add_subparsers(dest="command")


csv2json_parser = subparsers.add_parser("csv2json", help="Перевести csv в json")
add_command_parsers(csv2json_parser)


json2csv_parser = subparsers.add_parser("json2csv", help="Перевести json в csv")
add_command_parsers(json2csv_parser)


csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Перевести csv в xlsx")
add_command_parsers(csv2xlsx_parser)


args = parser.parse_args()
if args.command == "json2csv":
    json_to_csv(args.input, args.output)
elif args.command == "csv2json":
    csv_to_json(args.input, args.output)
elif args.command == "csv2xlsx":
    csv_to_xlsx(args.input, args.output)

```


```python
import argparse
from src.lib.text import count_freq, top_n, normalize, tokenize

parser = argparse.ArgumentParser(description="CLI для работы с текстовыми файлами")
subparsers = parser.add_subparsers(dest="command")


stats_parser = subparsers.add_parser("stats", help="Вывод топ слов")
stats_parser.add_argument("--input", required=True, type=str, help="Путь к входному файлу")
stats_parser.add_argument("--top", default=5, type=int, help="Сколько первых слов нужно")

cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
cat_parser.add_argument("--input", required=True, type=str, help="Путь к входному файлу")
cat_parser.add_argument("-n", action="store_true", help="Использовать нумерацию или нет")


args = parser.parse_args()
if args.command == "stats":
    with open(args.input, "r", encoding="utf-8") as f:
        text = f.read()
    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freq(tokens)
    if args.top:
        freq = top_n(freq, args.top)
    else:
        freq = top_n(freq)
    for (word, count) in freq:
        print(f"{word}: {count}")
elif args.command == "cat":
    with open(args.input, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f):
            if args.n:
                print(f"{line_number}: {line}", end="")
            else:
                print(line, end="")
```
![CLI_CONVERT](/images/LAB06:CLI_CONVERTСнимок%20экрана%202025-11-19%20в%2011.22.48 AM.png)
![CLI_CONVERT](/images/LAB06:CLI_CONVERTСнимок%20экрана%202025-11-19%20в%2011.24.00 AM.png)
![CLI_CONVERT](/images/LAB06:CLI_CONVERTСнимок%20экрана%202025-11-19%20в%2011.24.19 AM.png)
![CLI_CONVERT](/images/LAB06:CLI_CONVERTСнимок%20экрана%202025-11-19%20в%2011.25.08 AM.png)
![CLI_TEXT](/images/LAB06:CLI_TEXTСнимок%20экрана%202025-11-19%20в%2011.20.47 AM.png)
![CLI_TEXT](/images/LAB06:CLI_TEXTСнимок%20экрана%202025-11-19%20в%2011.21.31 AM.png)
![CLI_TEXT](/images/LAB06:CLI_TEXTСнимок%20экрана%202025-11-19%20в%2011.21.56 AM.png)
_______________________________________________________________________________________________
LAB07

```python
import json, csv
from pathlib import Path
import pytest
from src.lab05.json_csv import json_to_csv, csv_to_json


def write_json(path: Path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"}


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2
    assert set(obj[0]) == {"name", "age"}


def test_json_to_csv_invalid_json(tmp_path: Path):
    src = tmp_path / "invalid.txt"
    src.write_text("invalid content", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_json_to_csv_invalid_csv(tmp_path: Path):
    csv_path = tmp_path / "invalid.txt"
    csv_path.write_text("invalid content", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(tmp_path / "input.json", str(csv_path))


def test_json_to_csv_not_exist(tmp_path: Path):
    src = tmp_path / "no_exist.json"
    with pytest.raises(FileNotFoundError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_json_to_csv_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_suffix_json(tmp_path: Path):
    json_invalid = tmp_path / "invalid.txt"
    json_invalid.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(tmp_path / "input.csv", json_invalid)


def test_csv_to_json_suffix_csv(tmp_path: Path):
    csv_invalid = tmp_path / "invalid.txt"
    csv_invalid.write_text("1,2", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(csv_invalid, str(tmp_path / "out.json"))


def test_csv_to_json_no_header_raises(tmp_path: Path):
    src = tmp_path / "bad.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
```
____________

```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "src,expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(src, expected):
    assert normalize(src) == expected


@pytest.mark.parametrize(
    "src,expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize(src, expected):
    assert tokenize(src) == expected


def test_count_and_top():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_tie_breaker():
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]
```
![black](/images/Lab07.black.png)
![testjson](/images/LAB07.TESTJSON.png)
![testtext](/images/LAB07.TESTTEXT.png)
____________________________________________________________________________________________________________________________________________________________________________
LAB08
```python
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

```








```python
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

```
![lab08](/images/lab08..png)
![lab08](/images/lab08.png)
__________________________________________________________________________________________________________________________________________________________________________
LAB09
```python
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
```
____________________________________________________________________________________________________________________________________________________________________________
LAB10.
```python
from collections import deque

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()
    
    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0
```





```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"[{self.value}]"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # ошибка: размер не обновляется
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка"""
        self._size += 1
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        self.tail.next = new_node
        self.tail = self.tail.next
        

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        self._size += 1
        new_node = Node(value, next=self.head)
        if self.head is None:
            self.tail = new_node
        self.head = new_node
        

    def remove_at(self, idx):
        """Удаление по индексу — неполная реализация, есть ошибки"""
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            if self._size == 1:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
            self._size -= 1
            return


        current = self.head
        for _ in range(idx - 1):
            current = current.next
        if self.tail == current.next:
            self.tail = current

        current.next = current.next.next
        self._size -= 1


    def insert(self, idx, value):
        """Вставка по индексу — неполная реализация, есть ошибки"""
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size


    
    def __repr__(self):
        """
          [A] -> [B] -> [C] -> None
        """
        current = self.head
        str = ""
        for _ in range(self._size):
            str += f"{current.value} -> "
            current = current.next
        return str + "None"

```