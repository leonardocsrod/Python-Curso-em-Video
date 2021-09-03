import math
num = int(input('Digit a number: '))
squareroot = math.sqrt(num)
print('The square root of {:.2f} is {:.2f}'.format(num, math.ceil(squareroot)))
