salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = salary - spend


for i in range(1, months):

    wastes = spend + (spend * increase)

    spend = wastes

    delt = salary - wastes

    money_capital1 = money_capital + delt

    money_capital = money_capital1

money_capital = - money_capital







# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
