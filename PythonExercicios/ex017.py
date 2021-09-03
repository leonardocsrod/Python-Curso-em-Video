from math import pow, sqrt, hypot
oppositecathetus = float(input('Lenght of the opposite cathetus: '))
adjacentcathetus = float(input('Lenght of the adjacent cathetus: '))
#hypotenuse = sqrt(pow(oppositecathetus, 2) + pow(adjacentcathetus, 2))
hypotenuse = hypot(oppositecathetus, adjacentcathetus)
print('The hypotenuse will measure: {:.2f}'.format(hypotenuse))
