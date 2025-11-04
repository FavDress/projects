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
    

        
