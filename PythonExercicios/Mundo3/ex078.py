'''
list = [0, 0, 0, 0, 0]
lower = 0
bigger = 0
list[0] = int(input('Digit a value - Position 0: '))
lower = list[0]
if list[0] > bigger:
    bigger = list[0]
list[1] = int(input('Digit a value - Position 1: '))
if list[1] < lower:
    lower = list[1]
if list[1] > bigger:
    bigger = list[1]
list[2] = int(input('Digit a value - Position 2: '))
if list[2] < lower:
    lower = list[2]
if list[2] > bigger:
    bigger = list[2]
list[3] = int(input('Digit a value - Position 3: '))
if list[3] < lower:
    lower = list[3]
if list[3] > bigger:
    bigger = list[3]
list[4] = int(input('Digit a value - Position 4: '))
if list[4] < lower:
    lower = list[4]
if list[4] > bigger:
    bigger = list[4]
print(list)
print(f'The lower is {lower}')
print(f'The bigger number is {bigger}')
'''
list_number = []
lower = bigger = 0
for c in range(0, 5):
    list_number.append(int(input(f'Digit a number - position {c}: ')))
    if c == 0:
        lower = bigger = list_number[c]
    else:
        if list_number[c] < lower:
            lower = list_number[c]
        if list_number[c] > bigger:
            bigger = list_number[c]
print(list_number)
print(f'The lowest number is {lower}')
print(f'The biggest number is {bigger}')
