class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return True

    def add(self, value):
        if isinstance(value, int):
            self.floors += value
        return self

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.floors + value)
        return NotImplemented

    def __radd__(self, value):
        return self.add(value)

    def __iadd__(self, value):
        return self.add(value)


# Пример выполнения кода
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # eq

h1 = h1 + 10  # add
print(h1)

print(h1 == h2)

h1 += 10  # iadd
print(h1)

h2 = 10 + h2  # radd
print(h2)

print(h1 > h2)  # gt
print(h1 >= h2)  # ge
print(h1 < h2)  # lt
print(h1 <= h2)  # le
print(h1 != h2)  # ne

### Пояснение кода:
# 1. **Конструктор** `__init__`: инициализирует название дома и количество этажей.
# 2. **Метод `__str__`**: возвращает строковое представление объекта для удобного вывода.
# 3. **Сравнительные методы** (`__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__ne__`):
# реализуют логику сравнения объектов `House` по количеству этажей, проверяя тип других объектов.
# 4. **Методы арифметических операторов** (`add`, `__radd__`, `__iadd__`):
# позволяют увеличивать количество этажей как с помощью обычного сложения, так и с помощью оператора `+=`.

### Изменения:
# 1. **Добавлен метод `__add__`**:
# Этот метод позволяет использовать оператор `+` для объектов класса `House` и целых чисел.
# Он создает новый объект `House` с увеличенным количеством этажей.
# 2. **Метод `__radd__`** остается без изменений и вызывает `add`, что позволяет использовать `int + House`.
