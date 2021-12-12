print('P.A. CREATOR')
firstTerm= int(input('First term: '))
ratio = int(input('Ratio: '))
count = 0
term = firstTerm
newPa = 10
total = 0
while newPa != 0:
    total = total + newPa
    while count <= total:
        print('{} - '.format(term), end='')
        count += 1
        term += ratio
    print('PAUSE\n')
    newPa = int(input('How many terms do you want to show more: '))
print('The progression finished with {} terms showed.'.format(total))  
