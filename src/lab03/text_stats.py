from  lib.text  import count_freq, top_n, normalize, tokenize


data = input()
data_normalized = normalize(data)
tokens = tokenize(data_normalized)
stats = count_freq(tokens)
top = top_n(stats)
print(f"Всего слов: {len(tokens)}\nУникальных слов: {len(stats)}\nТоп-5:")
for elm in top:
    print(f"{elm[0]}:{elm[1]}")