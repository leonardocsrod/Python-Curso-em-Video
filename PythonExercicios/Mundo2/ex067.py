'''Programa tabuada
encerra quando pede tabuada de valor negativo
usando while True'''


while True:
    print('-' * 45)
    timesTables = int(input('Do you want to see witch times tables: '))
    print('-' * 45)
    if timesTables < 0:
        break
    for c in range(1, 11):
        print(f'{timesTables} X {c} = {timesTables * c}')
        c += 1
print('Program TimesTables Finished. Thanks!')
