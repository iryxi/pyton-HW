#NBIbd-04-22 Egorov Artem Andreevich
a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третие число "))

minimum = min(a, b, c)
maximum = max(a, b, c)

result = [minimum, (a + b + c - minimum - maximum), maximum]
print("Порядок чисел", result)
