#NBIbd-04-22 Egorov Artem Andreevich
seconds = int(input("Введите временной промежуток в секундах "))

days = seconds // (24 * 3600)
seconds = seconds % (24 * 3600)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print("{:d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds))
