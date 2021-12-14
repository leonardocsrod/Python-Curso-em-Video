"""
counter = 1
while counter <= 10:
    print(counter, end=' ')
    counter += 1
print('The end')

while True:
    print(counter, end=" ")
number = 0
while number != 999:
    number = int(input('Write a number: '))
"""
counter = 0
sum1 = 0
while True:
    number = int(input('Write a number: '))
    if number == 999:
        break
    sum1 += number
#print('The sum is {}.'.format(sum1))
print(f'The sum is {sum1}.')
