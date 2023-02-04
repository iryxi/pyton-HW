#NBIbd-04-22 Egorov Artem Andreevich
days = int(input("Введите количество дней "))
hours = int(input("Введите количество часов "))
minutes = int(input("Введите количество минут "))
seconds = int(input("Введите количество секунд "))

total_seconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds

print("Общее количество секунд ", total_seconds)
