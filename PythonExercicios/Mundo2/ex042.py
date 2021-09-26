side1 = float(input('Inform the side A: '))
side2 = float(input('Inform the side B: '))
side3 = float(input('Inform the side C: '))

if (side1 < (side2 + side3)) and (side2 < (side1 + side3)) and (side3 < (side2 + side1)):
    print('The sides form a triangle!')
    if side1 != side2 and side1 != side3 and side2 != side3:
        print('The triangle is ESCALENO!')
    elif side1 == side2 and side1 == side3 and side2 == side3:
        print('the triangle is EQUILATERO!')
    elif (side1 == side2 and side1 != side3) or (side2 == side3 and side2 != side1) or (side1 == side3 and side1 != side2):
        print('the triangle is ISOSCELES!')
else:
    print('The sides aren´t a triangle!')  
 