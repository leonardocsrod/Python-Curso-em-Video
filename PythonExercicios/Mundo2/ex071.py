bank = 'CEV BANK'
print('=' * 15)
print('{:^15}'.format(bank))
print('=' * 15)
valor = int(input('How much money do you want to get: R$ '))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R$ {cedula:.2f}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('Caixa encerrado!')