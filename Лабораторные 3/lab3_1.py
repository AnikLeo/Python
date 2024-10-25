# TODO Напишите функцию для поиска индекса товара
def items_index(items_list, find_item):
    if find_item in items_list:
        index = items_list.index(find_item)
    else:
        index = None

    return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = items_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
