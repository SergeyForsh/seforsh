def calculate_structure_sum(data):
    total = 0

    for item in data:
        if isinstance(item, int):  # Проверка, является ли элемент целым числом
            total += item
        elif isinstance(item, str):  # Проверка, является ли элемент строкой
            total += len(item)
        elif isinstance(item, list) or isinstance(item, tuple):  # Проверка, является ли элемент списком или кортежем
            total += calculate_structure_sum(item)  # Рекурсивный вызов для вложенных структур
        elif isinstance(item, dict):  # Проверка, является ли элемент словарём
            total += calculate_structure_sum(item.keys())  # Суммируем ключи словаря
            total += calculate_structure_sum(item.values())  # Суммируем значения словаря

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

print()

def calculate_structure_sum(data):
    total = 0

    for item in data:
        if isinstance(item, int):  # Проверка, является ли элемент целым числом
            total += item
        elif isinstance(item, str):  # Проверка, является ли элемент строкой
            total += len(item)
        elif isinstance(item, list) or isinstance(item, tuple):  # Проверка, является ли элемент списком или кортежем
            total += calculate_structure_sum(item)  # Рекурсивный вызов для вложенных структур
        elif isinstance(item, dict):  # Проверка, является ли элемент словарём
            total += calculate_structure_sum(item.keys())  # Суммируем ключи словаря
            total += calculate_structure_sum(item.values())  # Суммируем значения словаря
        elif isinstance(item, set):  # Проверка, является ли элемент множеством
            total += calculate_structure_sum(item)  # Рекурсивный вызов для множеств

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый результат: 99
