class Animal:
    def __init__(self, name):
        self.alive = True  # Живой
        self.fed = False   # Накормленный
        self.name = name   # Индивидуальное название животного


class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name     # Индивидуальное название растения


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False  # Цветы не съедобные


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобные


# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Примеры использования
print(a1.name)         # Выводит: Волк с Уолл-Стрит
print(p1.name)         # Выводит: Цветик семицветик
print(a1.alive)        # Выводит: True
print(a2.fed)          # Выводит: False

a1.eat(p1)             # Выводит: Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)             # Выводит: Хатико съел Заводной апельсин

print(a1.alive)        # Выводит: False
print(a2.fed)          # Выводит: True