height = int(input("Введите Ваш рост (см): " ))
weight = float(input("Введите Ваш вес (кг): " ))
age = int(input("Введите Ваш возраст (лет): "))
gender = input("Введите Ваш пол (м/ж): " )

height_m = height / 100

imt = round(weight / height_m ** 2, 2)

if gender == 'ж':
    if 19 <= age <= 24:
        if 19 <= imt <= 24:
            print('Нормальная масса тела')
        elif imt < 19:
            add_w = round(((19 - imt)*height_m**2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 24:
            add_w = round(((24 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if 25 <= age <= 34:
        if 20 <= imt <= 25:
            print('Нормальная масса тела')
        elif imt < 20:
            add_w = round(((20 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 25:
            add_w = round(((25 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if 35 <= age <= 44:
        if 21 <= imt <= 26:
            print('Нормальная масса тела')
        elif imt < 21:
            add_w = round(((21 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 26:
            add_w = round(((26 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if 45 <= age <= 54:
        if 22 <= imt <= 27:
            print('Нормальная масса тела')
        elif imt < 22:
            add_w = round(((22 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 27:
            add_w = round(((27 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if 55 <= age <= 64:
        if 23 <= imt <= 28:
            print('Нормальная масса тела')
        elif imt < 23:
            add_w = round(((22 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 28:
            add_w = round(((28 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if  age > 65:
        if 24 <= imt <= 29:
            print('Нормальная масса тела')
        elif imt < 24:
            add_w = round(((22 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 29:
            add_w = round(((29 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)

else:
    if 19 <= age <= 24:
        if 20 <= imt <= 25:
            print('Нормальная масса тела')
        elif imt < 20:
            add_w = round(((20 - imt)*height_m**2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 25:
            add_w = round(((25 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if 25 <= age <= 34:
        if 21 <= imt <= 26:
            print('Нормальная масса тела')
        elif imt < 21:
            add_w = round(((21 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 26:
            add_w = round(((26 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if 35 <= age <= 44:
        if 22 <= imt <= 27:
            print('Нормальная масса тела')
        elif imt < 22:
            add_w = round(((22 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 27:
            add_w = round(((27 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if 45 <= age <= 54:
        if 23 <= imt <= 28:
            print('Нормальная масса тела')
        elif imt < 23:
            add_w = round(((23 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 28:
            add_w = round(((28 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if 55 <= age <= 64:
        if 24 <= imt <= 29:
            print('Нормальная масса тела')
        elif imt < 24:
            add_w = round(((24 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 29:
            add_w = round(((29 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)
    if  age > 65:
        if 25 <= imt <= 30:
            print('Нормальная масса тела')
        elif imt < 25:
            add_w = round(((25 - imt) * height_m ** 2), 2)
            print("Недостаточный вес, до нормы необходимо добавить вес на", add_w, 'кг до', weight + add_w)
        elif imt > 30:
            add_w = round(((30 - imt) * height_m ** 2), 2)
            print("Избыточный вес, до нормы необходимо уменьшить вес на", add_w, 'кг до', weight + add_w)








