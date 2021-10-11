soma = 0
for c in range(1, 7):
    number = int(input('Digit a {} number: '.format(c)))
    if number % 2 == 0:
        soma += number
print('The sum is {}.'.format(soma))
