import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_color(self, *rgb):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in rgb)

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            super().__init__(color, *([sides[0]] * self.sides_count))
        else:
            super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


# Примеры использования и проверки:

circle1 = Circle((200, 200, 100), 10)  # Цвет, длина окружности
cube1 = Cube((222, 35, 130), 6)        # Цвет, сторона куба

# Изменение цвета:
circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

# Длина окружности:
print(len(circle1))

# Объём куба:
print(cube1.get_volume())

# Объяснение кода:
# КлассFigure :

# Инкапсулированные атрибуты: __sidesи __color.
# Методы установки и получения цветов, а также сторонние проверки на корректность.
# Метод __len__восстановления периметра фигуры.
# КлассCircle :

# Унаследован от Figure, имеет метод расчета площади круга.
# Радиус рассчитывается через длину окружности.
# КлассTriangle :

# В результате Figureиспользования формулы Герона для вычисления площади.
# КлассCube :

# Унаследовано от Figure, переопределяет список сторон для куба и добавляет метод для расчета объема.
# Вывод кода:
# Этот код создает объекты проверки и методы работы, методы изменения цвета и стороны, вычисления периметра и площади.
