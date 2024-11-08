# def summa(n):
#     if n == 0:
#          return 0
#     else:
#          return n + summa(n - 1)
# print(summa(5))
# print()
# stack = []
# stack.append(1)
# print('Добавили элемент' , stack)
# stack.append(2)
# print('Добавили элемент' , stack)
# stack.append(3)
# print('Добавили элемент' , stack)
# print(stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
print()
def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)
    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Получаем первую цифру
        first = int(str_number[0])
        # Рекурсивно вызываем функцию для оставшихся цифр
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1, возвращаем оставшуюся цифру
        return int(str_number)
# Пример вызова функции
result = get_multiplied_digits(40203)
print(result)  # Ожидаемый результат: 24

print()

print(get_multiplied_digits(123))  # Ожидаемый результат: 6 (1 * 2 * 3)
print(get_multiplied_digits(99))   # Ожидаемый результат: 81 (9 * 9)
print(get_multiplied_digits(5))    # Ожидаемый результат: 5 (осталась одна цифра)
