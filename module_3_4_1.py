def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()  # Приводим корневое слово к нижнему регистру
    for word in other_words:
        word_lower = word.lower()  # Приводим каждое слово из других слов к нижнему регистру
        # Проверяем, содержится ли корневое слово в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в список, если условие выполняется
    return same_words
# Примеры вызовов функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# Вывод результатов
print(result1)  # Ожидаемый результат: ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидаемый результат: ['Able', 'Disable']

### Объяснение кода:
# 1. Функция `single_root_words` принимает корневое слово `root_word`
#    и неограниченное количество других слов через `*other_words`.
# 2. Создается пустой список `same_words`, в который будут добавляться подходящие слова.
# 3. Корневое слово приводится к нижнему регистру для корректного сравнения.
# 4. Цикл `for` перебирает каждое слово из `other_words`, также приводя его к нижнему регистру.
# 5. Условие проверяет, содержится ли корневое слово в текущем слове или наоборот.
#    Если условие выполняется, слово добавляется в список `same_words`.
# 6. Функция возвращает список `same_words`.
