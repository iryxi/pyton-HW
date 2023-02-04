#NBIbd-04-22 Egorov Artem Andreevich
import math

R = float(input("Введите радиус цилиндра "))
H = float(input("Введите высоту цилиндра "))

base_area = math.pi * R ** 2
V = base_area * H

print("Объём цилиндра ", V)
