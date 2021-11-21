from time import sleep
number1 = int(input('First number: '))
number2 = int(input('Second number: '))
menu = 0
while menu != 5:
    print('Menu')
    print('\33[33m[1]\33[m Somar')
    print('\33[33m[2]\33[m Multiplicar')
    print('\33[33m[3]\33[m Maior')
    print('\33[33m[4]\33[m Novos números')
    print('\33[33m[5]\33[m Sair do programa')
    menu = int(input('Choose a number: '))
    if menu == 1:
        sum = number1 + number2
        print('The result of sum is {}.'.format(sum))
    elif menu == 2:
        multiplication = number1 * number2
        print('The result of multiplication is {}.'.format(multiplication))
    elif menu == 3:
        if number2 > number1:
            bigger = number2
        else:
            bigger = number1
            print('The bigger number is {}.'.format(bigger))
    elif menu == 4:
        number1 = int(input('First number: '))
        number2 = int(input('Second number: '))
    elif menu == 5:
        print('Ending...')
    else:
        print('This option {} is not valid.'.format(menu))
    sleep(2)        
print('The end! Thanks.')
