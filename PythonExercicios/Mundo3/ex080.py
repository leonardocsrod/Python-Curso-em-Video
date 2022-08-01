lista = []
for c in range(0, 5):
    n = int(input('Digit a value: '))
    if c==0 or n > lista[-1]:
        lista.append(n)
        print(f'Added in the end of the list!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Added in the position {pos}!')
                break
            pos +=1
print('-=' * 30)
print(f'The digited value were: {lista}')
