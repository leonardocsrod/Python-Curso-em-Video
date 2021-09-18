width = float(input("Digit the width: "))
height = float(input('Digit the hegth: '))
area = width * height
qink = area / 2
print('Your wall has {:.2f} x {:.2f}, and the area is {}.'.format(width, height, area))
print('You will need {:.2f} lts of ink.'.format(qink))