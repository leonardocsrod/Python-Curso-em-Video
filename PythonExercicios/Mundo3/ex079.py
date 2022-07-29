numbers = list()
while True:
    listNumber = int(input('Digit a number: '))
    if listNumber not in numbers:
        numbers.append(listNumber)
        print('The nember was added.')
    else:
        print('The number already is in the list!')
    answerContinue = str(input('Do you want to continue[y/n]: '))
    if answerContinue in 'nN':
            break
    if answerContinue not in 'yY':
        print('The value is invalid.')
        answerContinue = str(input('Do you want to continue[y/n]: '))
        if answerContinue in 'nN':
            break
        
print('-=' * 30)
numbers.sort()
print(f'You digited the values: {numbers}')
