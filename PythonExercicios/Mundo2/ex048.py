soma = 0
counter = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        counter += 1
        soma += c 
print('Sum = {} and counter = {}'.format(soma, counter))
