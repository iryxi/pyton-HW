#NBIbd-04-22 Egorov Artem Andreevich
inchperfoot = 12
yardperfoot = 0.33333
mileperfoot = 0.000189394

feet = float(input("Введите дистанцию в футах "))

inches = feet * inchperfoot
yards = feet * yardperfoot
miles = feet * mileperfoot

print("Дюймы", inches)
print("Ярды", yards)
print("Мили", miles)