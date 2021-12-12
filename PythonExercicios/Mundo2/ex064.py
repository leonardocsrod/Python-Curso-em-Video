number = counter = sum1 = 0
number = int(input('Write a number [999 to stop]: '))
while number != 999:
    counter += 1
    sum1 += number
    number = int(input('Write a number [999 to stop]: '))
print('You writed {} number(s) and the sum was {}!'.format(counter, sum1))
