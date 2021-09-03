import math
angle = float(input("Write the angle: "))
print("The angle {:.2f} has the sin {:.2f}, cos {:.2f}, tan {:.2f}.".format(angle, math.sin(math.radians(angle)), math.cos(math.radians(angle)), math.tan(math.radians(angle))))
