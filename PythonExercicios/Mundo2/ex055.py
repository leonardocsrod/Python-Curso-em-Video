bigger_weight = 0
smaller_weight = 1000
for c in range(1, 6):
    weight = float(input('Weight of {}º person: '.format(c)))
    if c == 1:
        bigger_weight = weight
        smaller_weight = weight
    else:
        if weight > bigger_weight:
            bigger_weight = weight            
        elif  weight < smaller_weight:
            smaller_weight = weight

print('The bigger weight was {:.2f} and the smaller weight was {:.2f}!'.format(bigger_weight, smaller_weight))
