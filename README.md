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