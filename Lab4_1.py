import json

file_path = 'input.json'

def sum_of_products(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        data = json.load(f)

    total_sum = sum(item['score'] * item['weight'] for item in data)

    return round(total_sum, 3)

result = sum_of_products(file_path)
print(result)