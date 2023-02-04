#NBIbd-04-22 Egorov Artem Andreevich
reg_price = 3.49
discount = 0.6

quantity = int(input("Количество приобретенных вчерашних буханок хлеба "))

discounted_price = reg_price * (1 - discount)
total_cost = discounted_price * quantity

print("обычная цена $ {:.2f}".format(reg_price))
print("цена со скидкой $ {:.2f}".format(discounted_price))
print("общая стоимость приобретенного хлеба $ {:.2f}".format(total_cost))
