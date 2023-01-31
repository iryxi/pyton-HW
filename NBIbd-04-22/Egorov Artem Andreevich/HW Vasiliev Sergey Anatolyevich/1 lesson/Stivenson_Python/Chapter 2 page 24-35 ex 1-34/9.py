#NBIbd-04-22 Egorov Artem Andreevich
x = float(input())
q = (x * 0.04) + x
w = (q * 0.04) + q
e = (w * 0.04) + w
r = (e * 0.04) + e
print('после первого года', round(q,2))
print('после второго года', round(w,2))
print('после третьего года', round(e,2))
print('после четвертого года', round(r,2))
