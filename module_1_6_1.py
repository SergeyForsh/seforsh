my_dict= {'Sergey': 1966, 'Elena': 1969, 'Dima': 1987, 'Evgeniy': 1988}
print(my_dict)
del my_dict ['Dima']
print(my_dict)
print(my_dict.values())
my_set = {1,2,3,4,5,1,2,3,'String', True, (1,2,3)}
print(my_set)
print(my_set.add(10))
print(my_set)
print()
my_dict = {'Sergey': 1966, 'Elena': 1969, 'Dima': 1987, 'Evgeniy': 1988}
print('Словарь:', my_dict)
print('Год рождения Sergey:', my_dict['Sergey'])
print('Год рождения Elena:', my_dict.get('Elena', 'нет такого ключа'))
my_dict.update({'Dima': 1987, 'Evgeniy': 1988})
removed_year = my_dict.pop('Dima')
print('Значение удалённого элемента \'Dima\':', removed_year)
print('Изменённый словарь:', my_dict)
print()
my_set = {2, 3, 3, 2, True, True, False, True, 'list', 'set', 'list', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:', my_set)


