import random

numbers = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
#print(numbers)
print('Os valores sorteados foram: ', end='')
bigger_number = numbers[0]
smaller_number = numbers[0]
for n in range(0, 5):
    if numbers[n] < smaller_number:
        smaller_number = numbers[n]
    if numbers[n] > bigger_number:
        bigger_number = numbers[n]
    print(f'{numbers[n]} ', end='')
print('\n')
#print(f'The bigest value is {max(numbers)}')
#print(f'The smaller value is {min(numbers)}')
print(f'The bigest value is {bigger_number}')
print(f'The smaller value is {smaller_number}')
