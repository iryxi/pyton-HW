#NBIbd-04-22 Egorov Artem Andreevich
from math import*
import math
n = int(input())
print(n//3600,'прошло часов')
print(n % 60,'полных секунд прошло с начала очередной минуты')
print((n//3600)//60,' полных минут прошло с начала очередного часа')