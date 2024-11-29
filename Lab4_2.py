import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file) -> None:
    with open(csv_file, 'r', encoding='utf=8') as f:
        reader = csv.DictReader(f)
        json_data = [row for row in reader]

    OUTPUT_FILENAME = json.dumps(json_data, indent=4)

    print (OUTPUT_FILENAME)

result = task(INPUT_FILENAME)
print(result)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
