print('\033[32m-\033[m' * 20)
print('\033[33mFibonacci Sequence\033[m')
print('\033[32m-\033[m' * 20)
terms = int(input('How many terms do you want to show: '))
firstTerm = 0
secondTerm = 1
thirdTerm = 0
count = 3
print('{} -'.format(firstTerm), end = ' ')
print('{} -'.format(secondTerm), end = ' ')
while count <= terms:
    
    thirdTerm = firstTerm + secondTerm
    print('{} -'.format(thirdTerm), end = ' ')
    firstTerm = secondTerm
    secondTerm = thirdTerm
    count += 1
print('The end')
