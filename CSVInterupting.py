import csv


def write_rows_to_csv(name, rows: list) -> None:
    with open(name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)


def list_read_from_csv(name) -> list:
    ans = []
    with open(name, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter=';', quotechar='"')
        for row in reader:
            ans.append(row)
    return ans


def dict_read_from_csv(name) -> dict:
    ans = {}
    with open(name, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter=';', quotechar='"')
        for row in reader:
            ans[row[0]] = row[-1]
    return ans
