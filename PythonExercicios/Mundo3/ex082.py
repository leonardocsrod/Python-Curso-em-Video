list = []
oddList = []
pairList = []
while True:
    n = int(input('Digit a number: '))
    list.append(n)
    if n % 2 == 0:
        pairList.append(n)
    else:
        oddList.append(n)
    answer = str(input('Do you want to continue[y/n]: '))
    if answer not in 'yYnN':
        print('The value in not walid.')
        answer = str(input('Do you want to continue[y/n]: '))
    if answer in 'nN':
        break
print('-=' *30)
print(f'The complete list is {list}')
pairList.sort()
print(f'The pair list is {pairList}')
oddList.sort()
print(f'The odd list is {oddList}')

