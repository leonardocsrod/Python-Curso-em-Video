name = 'PRICE LIST'
print('-' * 40)
print(f'{name:^40}')
print('-' * 40)
price_list = (
    'Pen', 1.75,
    'Pencil', 2,
    'Rubber', 2.5,
    'Notebook', 15,
    'Bag', 40
)
for pos in range(0, len(price_list)):
    if pos % 2 == 0:
        print(f'{price_list[pos]:.<30}', end='')
    else:
        print(f'R${price_list[pos]:>7.2f}')
print('-' * 40)
