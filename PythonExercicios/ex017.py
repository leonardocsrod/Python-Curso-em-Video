import math
oppositecathetus = float(input('Inform the opposite cathetus: '))
sidecathetus = float(input('Inform the side cathetus:  '))
hypotenuse = math.hypot(oppositecathetus, sidecathetus)
print('The hypotenuse is {:.2f}'.format(hypotenuse))
