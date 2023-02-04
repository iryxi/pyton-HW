#NBIbd-04-22 Egorov Artem Andreevich
kilo = float(input("Введите значение в килопаскалях "))

psi = kilo * 0.145037738
mm_hg = kilo * 7.500616827
atm = kilo / 101.325

print("Значение в PSI ", psi)
print("Значение в миллиметрах ртутного столба ", mm_hg)
print("Значение в атмосферах ", atm)
