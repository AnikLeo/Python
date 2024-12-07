def calculator(num1: float, num2: float, operator: str) -> float:
    if operator == '+':
        return (f"Результат сложения равен: {num1 + num2}")
    elif operator == '-':
        return (f"Результат вычитания равен: {num1 - num2}")
    elif operator == "*":
        return (f"Результат умножения равен: {num1 * num2}")
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Ошибка: деление на ноль.")
        return (f"Результат деления равен: {num1 / num2}")
    else:
        raise ValueError("Ошибка: Недопустимая операция.")

def main():
    print("Вас приветствует калькулятор!")

    while True:
        try:
            num1 = float(input("Введите первое число:"))
            num2 = float(input("Введите второе число:"))
            operator = input("Введите знак операции +, -, *, /:")
            result = calculator(num1, num2, operator)
            print(f"Результат равен: {result}")
            break
        except ValueError as e:
            print(f"Неккоректный ввод: {e}, повторите ввод данных")

if __name__ == '__main__':
   main()
