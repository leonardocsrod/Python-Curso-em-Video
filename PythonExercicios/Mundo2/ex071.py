bank = 'CEV BANK'
nota50 = nota20 = nota10 = nota5 = nota1 = 0
value = 0
print('=' * 15)
print('{:^15}'.format(bank))
print('=' * 15)
value = int(input('How much money do you want to get: R$'))
while True:
    nota50 = value / 50
    if nota50 > 1:
        if value % 50 == 0:
            print(f'Nota de 50: {nota50} e acaba')
            break
        if nota50 > 0:
            print(f'Nota de 50: {nota50:.0f} e falta troco')
    #
    nota20 = (value % 50) / 20
    if nota20 % 20 == 0:
        print(f'Nota de 20: {nota20} e acaba')
        break
    if nota20 > 0:
        print(f'Nota de 20: {nota20:.0f} e falta troco')
    '''
    #
    nota10 = value / 10
    if value % 10 == 0:
        print(f'Nota de 10: {nota10}')
        break
    if nota10 > 0:
        print(f'Nota de 10: {nota10}')
    #
    nota5 = value / 5
    if value % 5 == 0:
        print(f'Nota de 5: {nota5}')
        break
    if nota5 > 0:
        print(f'Nota de 5: {nota5}')
    #
    nota1 = value / 1
    if value % 1 == 0:
        print(f'Nota de 10: {nota1}')
        break
    if nota10 > 0:
        print(f'Nota de 50: {nota1}')
        '''
    break


