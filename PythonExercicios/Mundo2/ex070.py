totalBuy = totalValue = 0
product = ' '
lowerProduct = ' '
lowerPrice = 0
count = 0
while True:
    print('-' * 20)
    print('LOJA SUPER BARATÃO')
    print('-' * 20)
    #
    price = 0
    product = str(input('Product name: '))
    price = float(input('Price: R$'))
    if count == 0:
        lowerProduct = product
        lowerPrice = price
        count += 1
    else:
        if price < lowerPrice:
            lowerPrice = price
            lowerProduct = product
    totalValue += price
    #choice logic
    choice = ' '
    while choice not in 'Y/N':
        choice = str(input('Do you want to continue[Y/N]: ')).strip().upper()[0]
    if choice == 'Y':
        totalBuy += 1
    if choice == 'N':
        break
print(f'Total Value: R${totalValue:.2f}')
print(f'Products buyed: {totalValue}')
print(f'Lower Product:{lowerProduct}, Lower Price: R${lowerPrice:.2f}')
