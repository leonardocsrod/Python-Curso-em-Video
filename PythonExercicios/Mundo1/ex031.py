distance = int(input('Inform the distance: '))
if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45
print('Your trip cost \033[1;33;44mR$ {:.2f}\033[m.'.format(price))
