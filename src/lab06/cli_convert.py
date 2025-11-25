import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def add_command_parsers(com_parser):
    com_parser.add_argument(
        "--input", required=True, type=str, help="Путь к входному файлу"
    )
    com_parser.add_argument(
        "--output", required=True, type=str, help="Путь к выходному файлу"
    )


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
