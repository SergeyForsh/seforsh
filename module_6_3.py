import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound if self.sound else "Silence...")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        number_of_eggs = random.randint(1, 4)
        print(f"Here are(is) {number_of_eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed / 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

# Пример использования классов
db = Duckbill(10)

print(db.live)  # True
print(db.beak)  # True
db.speak()  # Click-click-click
db.attack()  # Be careful, i'm attacking you 0_0
db.move(1, 2, 3)  # Двигаем утконоса
db.get_cords()  # X: 10 Y: 20 Z: 30
db.dive_in(6)  # Ныряем
db.get_cords()  # X: 10 Y: 20 Z: 0
db.lay_eggs()  # Откладываем яйца

### Объяснение кода:

# 1. **Класс `Animal`:**
#    - Основной класс для животных, содержит основные атрибуты и методы.
#    - Атрибуты инициализируются в конструкторе, в том числе координаты и скорость.
#    - Методы `move`, `get_cords`, `attack` и `speak` реализованы в соответствии с заданием.
#
# 2. **Класс `Bird`:**
#    - Наследуется от `Animal` и добавляет атрибут `beak`.
#    - Метод `lay_eggs` выводит случайное количество яиц.
#
# 3. **Класс `AquaticAnimal`:**
#    - Наследуется от `Animal` и изменяет степень опасности.
#    - Метод `dive_in` изменяет координату Z, учитывая скорость.
#
# 4. **Класс `PoisonousAnimal`:**
#    - Наследуется от `Animal` и задает высокую степень опасности.
#
# 5. **Класс `Duckbill`:**
#    - Наследует от `Bird`, `AquaticAnimal` и `PoisonousAnimal`.
#    - Задает звук, который издает утконос.
#
# ### Пример работы программы:
# - Создается объект `Duckbill`, и выполняются последовательные вызовы методов,
# которые показывают поведение утконоса.