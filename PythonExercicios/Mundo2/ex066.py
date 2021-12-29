number = 0
counter = 0
sum1 = 0
while True:
    number = int(input('Write a number[999 to stop]: '))
    if number == 999:
        break
    sum1 += number
    counter += 1
print(f'You wrote {counter} numbers and the sum was {sum1}.')
