users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dict_site = {"Общее количество" : 0, "Уникальные посещения" : 0}

dict_site["Общее количество"] = len(users)

dict_site["Уникальные посещения" ] = len(set(users))

print(dict_site)