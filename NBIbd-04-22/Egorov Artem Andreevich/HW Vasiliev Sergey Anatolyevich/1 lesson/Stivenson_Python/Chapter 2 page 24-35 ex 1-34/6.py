#NBIbd-04-22 Egorov Artem Andreevich
amount = float(input('Сумма'))
tips = float(input('Чаевые')) 
tax = float(input('Налог')) 
wtips = (amount * tips)
wtax = (amount * tax)
result = amount + wtips + wtax
print(f'Сумма {amount:.2f} + Чаевые {wtips:.2f} + Налог {wtax:.2f} = ИТОГО {result:.2f}')

