'''
PythonExercicios\from math import factorial
number = int(input('Choose a number: '))
result = factorial(number)
print('The factorial of {}! is = {}'.format(number, result))
'''
number = int(input('Choose a number: '))
control = number
result = 1
print('Calculating {}! = '.format(number), end='')
while control > 0:
    if control > 1:
        print('{} X '.format(control), end='')
    else:
        print('{} = '.format(control), end='')
    if control > 0:
        result = result * control
        control -= 1
print('{}'.format(result)) 