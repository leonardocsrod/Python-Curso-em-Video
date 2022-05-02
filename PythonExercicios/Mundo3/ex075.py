cont_9 = 0
cont_even = 0
number_3 = 0

numbers= (
    (int(input('Digit a number[0-9]: '))), 
    (int(input('Digit another number[0-9]: '))), 
    (int(input('Digit another number[0-9]: '))),
    (int(input('Digit another number[0-9]: ')))
    )
print(f'You digit the numbers: {numbers}')
for n in range(0, 4):
    if numbers[n] == 9:
        cont_9 += 1
print(f'The number 9 shows {cont_9} times.')
#print(f'the number 9 shows up {numbers.count(9)} times.')
for n in range(0, 4):    
    if numbers[n] == 3:
        print(f'the number 3 shows in position {n+1}')
#print(f'the number 3 shows in position {numbers.index(3)}')
print(f'The even values digited was: ', end='')
for n in numbers:
    if n % 2 == 0:
        print(f'{n}', end=' ')
print('\n')
