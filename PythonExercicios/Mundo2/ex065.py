number = counter = sum1 = average = lower1 = upper1 = 0
decisor = 's'
while decisor in 'Ss':
    number = int(input('Write a number: '))
    counter += 1
    sum1 += number
    average = sum1 / counter
    if counter == 1:
        lower1 = upper1 = number
    else:
        if number > upper1:
            upper1 = number
        if number < lower1:
            lower1 = number  
    decisor = str(input('Do you want to continue[S/N]: ')).lower().strip()
print('You writed {} number(s) and the average was {:.2f}!'.format(counter, average))
print('The upper value was {} and de lower was {}!'.format(upper1, lower1))
