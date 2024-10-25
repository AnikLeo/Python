# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, n = ","):
    part_first = participants_first_group.split(n)
    part_second = participants_second_group.split(n)
    common_part = list(set(part_first).intersection(part_second))
    return common_part


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))

# TODO Проверьте работу функции с разделителем отличным от запятой
