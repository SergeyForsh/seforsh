fond= ['apple', 'coconut', 'banana']
print(fond)
fond= ['apple', 'coconut', 'banana']
print(fond [0])
fond= ['apple', 'coconut', 'banana']
fond [0]='peach'
print(fond)
fond [1]='peach'
print(fond)
fond= ['apple', 'coconut', 'banana']
fond .append(True)                    # метод1 добавить
print(fond)
fond= ['apple', 'coconut', 'banana']
fond .extend('kokacola')              # метод2
print(fond)
fond .extend(['kokacola' ,2])         # метод2-2
print(fond)
fond .remove('apple')                 # метод3
print(fond)
print('coconut' in fond)              # проверка элемента в списке (верно)
print('coconut' not in fond)          # проверка нет элемента...   (ложь)
print(fond [0:2])                 # срез
print(fond [0:2:2])               # срез с шагом 2
