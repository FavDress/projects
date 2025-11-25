import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")

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
