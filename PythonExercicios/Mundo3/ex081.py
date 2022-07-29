list = []
sum = 0
while True:
    n = int(input('Digit a value: '))
    list.append(n)
    sum += 1
    resp = str(input('Do you want to continue[y/n]: '))
    if resp not in 'yYnN':
        print('The value is not valid!')
        resp = str(input('Do you want to continue[y/n]: '))
    if resp in 'nN':
        break
print(f'You digit {sum} elements.')
print(f'The digited value were: {list}')



