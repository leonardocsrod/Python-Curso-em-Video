print('\033[1;33;40m=\033[m' * 30)
print('     \033[1;33;40m10 TERMOS DE UMA PA\033[m')
print('\033[1;33;40m=\033[m' * 30)
first_term = int(input('First term: '))
ratio = int(input('Ratio: '))
tenth = first_term + (10 - 1) * ratio
for c in range(first_term, tenth + 1, ratio):
    print('{}'.format(c))
print('Finished') 
