from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as file:
        res = file.read().replace("\n", " ")

    return res


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    if len(rows) > 0:
        for elm in rows:
            if len(rows[0]) != len(elm):
                raise ValueError

    with open(path, "w", newline="", encoding="utf-8") as file:
        wr = csv.writer(file, delimiter=",")
        if header is not None:
            wr.writerow(header)
        wr.writerows(rows)
