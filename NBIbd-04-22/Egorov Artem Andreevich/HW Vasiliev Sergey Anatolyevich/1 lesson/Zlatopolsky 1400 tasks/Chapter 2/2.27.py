#NBIbd-04-22 Egorov Artem Andreevich
from math import*
import math
x = float(input()) #нижнее основание
y = float(input()) #верхнее основание 
h = float(input()) #высота
a = (x - y) / 2 #основания получившихся треугольников (их 2)
c = sqrt(a*a + h*h) #гипотенузы - боковые стороны равнобердренной трапеции
print(c + c + y + x) #периметр = сумма боковых сторон + сумма основания т.е сумма всех сторон
#Вроде как точно такое же условие как и в 2.17