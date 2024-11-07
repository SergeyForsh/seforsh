# Шаг 1: Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')
# Вызовы функции с разным количеством аргументов
print_params()  # без аргументов
print_params(10)  # только a
print_params(10, 'другая строка')  # a и b
print_params(b=25)  # только b
print_params(c=[1, 2, 3])  # только c
# Шаг 2: Распаковка параметров
values_list = [3.14, 'текст', False]
values_dict = {'a': 42, 'b': 'словарь', 'c': None}
print("Распаковка из списка:")
print_params(*values_list)  # распаковка списка
print("Распаковка из словаря:")
print_params(**values_dict)  # распаковка словаря
# Шаг 3: Распаковка + отдельные параметры
values_list_2 = ['новая строка', 100]
print("Распаковка + отдельные параметры:")
print_params(*values_list_2, 42)  # распаковка списка и передача значения для a