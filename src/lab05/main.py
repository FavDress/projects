from src.lab05.csv_xlsx import csv_to_xlsx
from src.lab05.json_csv import json_to_csv, csv_to_json
csv_to_xlsx('data/samples/cities.csv','data/out/ch.xlsx')
json_to_csv('data/samples/people.json','data/out/ll.csv')
csv_to_json('data/samples/people.csv','data/out/nn.json')
