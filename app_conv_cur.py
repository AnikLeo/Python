# TODO опишите здесь функции для решения задачи
import json
import os
import requests
import pprint

def input_key(key_access):
    key = input("Введите API ключ:")
    with open(key_access, "w") as f:
        f.write(key)
    return key

def load_key(key_access):
    if os.path.exists(key_access):
        with open(key_access, "r") as f:
            key = f.read().strip()
            return key if key else input_key(key_access)
    else:
        return load_key(key_access)

def load_currencies(cur_json):
    with open(cur_json, 'r', encoding="utf-8") as f:
        data = json.load(f)
        currency_l = data['валюты']
        list_cur = [currency['код'] for currency in currency_l if 'код' in currency]
        return list_cur

def get_conv_rate(base_currency, key):
    url = f"https://v6.exchangerate-api.com/v6/{key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    conversion_rate_dict = data['conversion_rates']
    return conversion_rate_dict

def valid_currency(currency, currencies):
    while not currency in currencies:
        print("Некорректный ввод валюты")
        currency = input("Введите конвертируемую валюту (например: RUB, USD и т.д). : ").strip().upper()

def convert(base_currency, target_currency, sum, key):
    rate = get_conv_rate(base_currency, key)
    if base_currency == target_currency:
        return sum
    if base_currency not in rate or target_currency not in rate:
        raise ValueError("Неверная валюта")
    return sum * rate[target_currency]

def main():
    print("Вас приветствует конвертер валют!")

    key = load_key('key_access.txt')
    currencies = load_currencies('currency.json')
    
    base_currency = input("Введите конвертируемую валюту (например: RUB, USD и т.д). : ").strip().upper()
    valid_currency(base_currency, currencies)


    target_currency = input("Введите валюту в которую необходимо сконвертировать (например: RUB, USD и т.д). : ").strip().upper()
    valid_currency(target_currency, currencies)
    
    while True:
        sum_input = input("Введите сумму: ")
        try:
            sum= float(sum_input)
            if sum <= 0:
                raise ValueError
            break
        except ValueError:
            print("Некорректная сумма, введите число больше 0.")

    result = convert(base_currency, target_currency, sum, key)

    print(f"За {sum} {base_currency} получите {result} {target_currency}")


if __name__ == '__main__':
    # TODO запустите здесь все необходимые функции
    main()
