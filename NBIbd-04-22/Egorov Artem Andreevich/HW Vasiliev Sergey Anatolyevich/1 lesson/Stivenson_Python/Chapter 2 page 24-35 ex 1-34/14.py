#NBIbd-04-22 Egorov Artem Andreevich
fttocm = 30.48
inchtocm = 2.54
ft = float(input("Впишите высоту в футах "))
inch = float(input("Впишите число в дюймах "))
height = (ft * fttocm + inch * inchtocm)
print("Высота в сантиметрах ", height)