#NBIbd-04-22 Egorov Artem Andreevich
import math

s = float(input("Введите длинну стороны многоугольника "))
n = int(input("Введите количество сторон многоугольника "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("Площадь многоугольника ", area)
