money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


count = 0

money = money_capital + salary


while money > spend:

    wastes = spend + (spend*increase)

    spend = wastes

    delt = salary - spend

    money1 = money + delt

    money = money1

    count += 1




# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", count)
