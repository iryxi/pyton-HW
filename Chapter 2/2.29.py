#NBIbd-04-22 Egorov Artem Andreevich
from math import*
import math
x = float(input()) 
y = float(input())
c = float(input()) 
u = float(input())
v = float(input()) 
i = float(input())
a = sqrt((c - x)*(c - x) + (u - y)*(u - y))
b = sqrt((v - c)*(v - c) + (i - u)*(i - u))
w = sqrt((v - x)*(v - x) + (i - y)*(i - y))
P = a + b + w
pp = P / 2
S = sqrt(pp*(pp - a)*(pp - b)*(pp - c))
print(P,"периметр")
print(S,"площадь")