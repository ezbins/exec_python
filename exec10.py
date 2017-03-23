#!/usr/bin/env python3
# coding: utf-8


prices = []
quantities = []


def checkNumberic(value):
    if value.isnumeric():
        return int(value)
    else:
        print("Please input numberic.")
        sys.exit()


def calcu_total(prices, quantities):
    for price, quantity in zip(prices, quantities):
        total_sum = total_sum + (price * quantity)

    return total_sum


print("Enter the price of item 1:", end=' ')
input_price_1 = input()
price1 = checkNumberic(input_price_1)
prices.append(price1)
print("Enter the quantity of item 1:", end=' ')
input_quantity_1 = input()
quantity1 = checkNumberic(input_quantity_1)
quantities.append(quantity1)

print("Enter the price of item 2:", end=' ')
input_price_2 = input()
price2 = checkNumberic(input_price_2)
prices.append(price2)
print("Enter the quantity of item 1:", end=' ')
input_quantity_2 = input()
quantity2 = checkNumberic(input_quantity_2)
quantities.append(quantity2)

print("Enter the price of item 3:", end=' ')
input_price_3 = input()
price3 = checkNumberic(input_price_3)
prices.append(price3)
print("Enter the quantity of item 3:", end=' ')
input_quantity_3 = input()
quantity2 = checkNumberic(input_quantity_3)
quantities.append(quantity3)

print("Subtotal {total}".format(total=calcu_total(prices, quantities)))
