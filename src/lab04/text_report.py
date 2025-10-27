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