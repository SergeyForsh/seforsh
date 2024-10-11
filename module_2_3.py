# import this
# name = input('Enter your name: ')
# if 5 > 1:      # таб или 4 пробела (правило написания)
#     print('ok')
#     print('not ok')
#     if 1 > 0:  # пробелы между операторами.
#                # если 1 > 5
#         print('I`m here')
# print()
# while 1 > 0:          # True. while True
#     number = int(input('Введите число: '))
#     if number % 2 == 0:
#         print('Число четное')
#     else:           # в остальных случаях не четное
#         print('Число не четное')
#         break
# print('Я за циклом')
# print()
# while 1 > 0:  # True. while True  Цикл: while
#     number = int(input('Введите число: '))
#     if number % 2 == 0:
#         print('Число четное')
#         continue  # Пропускает команды ниже и возвращается к верхней. Циклы break continue
#     else:  # в остальных случаях не четное
#         print('Число не четное')
#     print("Меня не забыли")
# print('Я за циклом')
#print()
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] >= 0:
        if my_list[i] != 0:
            print(my_list[i])
        i = i + 1
        continue
    else:
        break
print()
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0                           # определение длинны списка
while i < len(my_list):         # условия перебора списка
    if my_list[i] < 0:
        break
    if my_list[i] > 0:          # вывод результата
        print(my_list[i])
    i += 1

