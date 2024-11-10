
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызовем inner_function из test_function
    inner_function()

# Вызовем test_function, чтобы увидеть результат
test_function()

# Попробуем вызвать inner_function вне test_function
try:
    inner_function()  # Это вызовет ошибку
except NameError as e:
    print(f"Ошибка: {e}")

### Объяснение кода

# 1. Функция `test_function` определяет другую функцию `inner_function` внутри себя.
# 2. `inner_function` печатает строку "Я в области видимости функции test_function" при вызове.
# 3. `inner_function` вызывается внутри `test_function`, поэтому это работает.
# 4. Когда я пытаюсь вызвать `inner_function` вне `test_function`,
# Python выбрасывает ошибку `NameError`, потому что `inner_function` не доступна в глобальной области видимости.

