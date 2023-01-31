#NBIbd-04-22 Egorov Artem Andreevich
from math import*
import math
n = int(input())
k = int(input())
p = k / n
p1 = round(p)
s = k % n
print('Каждому по ', p1 ,'яблок')
print('Яблок останеться -',s)