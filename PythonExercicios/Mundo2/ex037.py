number = int(input('Digit a number: '))
print('\033[1;33;40m=+=\033[m' * 12)
print('[1] - Converta para binário')
print('[2] - Converta para octal')
print('[3] - Converta para hexadecimal')
print('\033[1;33;40m=+=\033[m' * 12)
option = int(input('Choose your option: '))
if option == 1:
    print('{} = {} binário'.format(number, bin(number)[2:]))
elif option == 2:
    print('{} = {} octal'.format(number, oct(number)[2:]))
elif option == 3:
    print('{} = {} binário'.format(number, hex(number)[2:]))
else:
    print('The number is not valid!')
