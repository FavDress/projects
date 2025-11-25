import argparse
from src.lib.text import count_freq, top_n, normalize, tokenize

parser = argparse.ArgumentParser(description="CLI для работы с текстовыми файлами")
subparsers = parser.add_subparsers(dest="command")


stats_parser = subparsers.add_parser("stats", help="Вывод топ слов")
stats_parser.add_argument(
    "--input", required=True, type=str, help="Путь к входному файлу"
)
stats_parser.add_argument(
    "--top", default=5, type=int, help="Сколько первых слов нужно"
)

cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
cat_parser.add_argument(
    "--input", required=True, type=str, help="Путь к входному файлу"
)
cat_parser.add_argument(
    "-n", action="store_true", help="Использовать нумерацию или нет"
)


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
    for word, count in freq:
        print(f"{word}: {count}")
elif args.command == "cat":
    with open(args.input, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f):
            if args.n:
                print(f"{line_number}: {line}", end="")
            else:
                print(line, end="")
