from text import normalize, top_n, count_freq, tokenize


def test_normalize():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка", yo2e=True) == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"


def test_top_n():
    assert top_n({"a": 3, "b": 2, "c": 1}, n=2) == [("a", 3), ("b", 2)]
    assert top_n({"aa": 2, "bb": 2, "cc": 1}, n=2) == [("aa", 2), ("bb", 2)]


def test_count_freq():
    assert count_freq(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}
    assert count_freq(["bb", "aa", "bb", "aa", "cc"]) == {"aa": 2, "bb": 2, "cc": 1}


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
