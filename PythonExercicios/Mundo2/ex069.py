counterEighteen = 0
mens = 0
woman20 = 0
while True:
    gender = ' '
    choice = ' '
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    age = int(input('Age: '))
    if age >= 18:
        counterEighteen += 1      
    while gender not in 'MF':
        gender = str(input('Gender[M/F]: ')).upper()[0]
    if gender == 'F' and age <= 20:
        woman20 += 1
    if gender == 'M':
        mens += 1      
    print('-' * 20)
    while choice not in 'SN':
        choice = str(input('Do you want continue[S/N]: ')).upper()[0]
    if choice == 'N':
        break
print(f'Minus eighteen people: {counterEighteen}')
print(f'Mens: {mens}')
print(f'Minus twenty women: {woman20}')
