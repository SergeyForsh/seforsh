class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Примеры использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# str
print(h1)  # Выводит: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Выводит: Название: ЖК Акация, кол-во этажей: 20

# len
print(len(h1))  # Выводит: 10
print(len(h2))  # Выводит: 20

### Объяснение добавленных методов:
# 1. **Метод `__len__`**: Этот метод возвращает количество этажей здания
# (атрибут `self.number_of_floors`). Он позволяет использовать функцию `len()` для объектов класса `House`.
# 2. **Метод `__str__`**: Этот метод возвращает строку с информацией о названии дома и количестве этажей.
# Он позволяет использовать функцию `print()` для объектов класса `House`, выводя их в удобочитаемом формате.