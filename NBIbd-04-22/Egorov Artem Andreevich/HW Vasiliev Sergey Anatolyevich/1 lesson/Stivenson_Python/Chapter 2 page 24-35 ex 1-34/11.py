#NBIbd-04-22 Egorov Artem Andreevich
mpg = float(input("Введите показатель потребления топлива в американских единицах: "))
lper100km = 235.215 / mpg
print("Показатель потребления топлива в канадских единицах: {:.2f} L/100 km".format(lper100km))
