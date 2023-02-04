#NBIbd-04-22 Egorov Artem Andreevich
mass = float(input("Введите массу воды  "))
delta_T = float(input("Введите разницу темпиратур в Цельсиях "))

specific_heat = 4.186
q = mass * specific_heat * delta_T

print("Затраты энергии", q, "Джоули")
cost = q / 1000 * 0.089
print("Стоймость $", cost)
