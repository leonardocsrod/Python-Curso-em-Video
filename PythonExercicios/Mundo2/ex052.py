import time
number = int(input('Digit a number: '))
counter = 0
for c in range(1, number + 1):
    
    if number % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ')
        counter += 1
    else:
        print('\033[34m{}\033[m'.format(c), end=' ')

print('')
if counter > 2:
    result = 'THE NUMBER ISN´T COUSIN'
else:
    result = 'THE NUMBER IS COUSIN'


print('The number {} is divisible {} times.'.format(number, counter))
print('{}'.format(result))
