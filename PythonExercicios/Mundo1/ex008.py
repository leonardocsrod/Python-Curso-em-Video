distance = float(input('Add a distance-meters: '))
print('The distance {:.2f} corresponds to: '.format(distance))
print('{:.2f}km'.format(distance/1000))
print('{:.2f}hm'.format(distance/100))
print('{:.2f}dam'.format(distance/10))
print('{:.2f}dm'.format(distance*10))
print('{:.2f}cm'.format(distance*100))
print('{:.2f}mm'.format(distance*1000))