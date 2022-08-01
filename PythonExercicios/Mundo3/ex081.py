list = []
while True:
    list.append(int(input('Digit a value: ')))
    resp = str(input('Do you want to continue[y/n]: '))
    if resp not in 'yYnN':
        print('The value is not valid!')
        resp = str(input('Do you want to continue[y/n]: '))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'You digit {len(list)} elements.')
list.sort(reverse=True)
print(f'The digited value were: {list}')
if 5 in list:
    print('the value 5 is in list')
else:
    print('The value 5 is not in list')



