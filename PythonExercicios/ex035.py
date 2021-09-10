print('\033[0;32;40m-=-\033[m' * 15)
print('              \033[0;33;40mTriangle analizer\033[m')
print('\033[0;32;40m-=-\033[m' * 15)
firstside = float(input('Write the first side: '))
secondside = float(input('Write the second side: '))
thirdside = float(input('Write the third side: '))

if firstside < (secondside + thirdside) and secondside < (thirdside + firstside) and thirdside < (secondside + firstside):
    print('It is a triangle!')
else:
    print('It is not a triangle!')
 