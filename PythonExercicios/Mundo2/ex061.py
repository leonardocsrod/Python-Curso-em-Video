print('P.A. CREATOR')
firstTerm = int(input("First term: "))
term = firstTerm
ratio = int(input('Ratio: '))
count = 1
while count <= 10:
    print('{} - '.format(term), end='')
    count += 1
    term += ratio
print('The end')
