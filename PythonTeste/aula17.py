num = (2, 5, 9, 1) #tupla
print(num)
#num[2] = 3 tupla não aceita substituição
num2 = [2, 5, 4, 1] #lista
print(num2)
num2[2] = 3 #lista aceita troca de item
print(num2)
num2.append(7) #adiciona item como último elemento
print(num2)
num2.sort() #coloca a lista em ordem crescente
print(num2)
num2.sort(reverse=True)
print(num2)
print(f'This lista has {len(num2)} elements.')
num2.insert(2, 0) #insere elemento na posição 2, valor 0
print(num2)
num2.pop() #elimina o último valor da lista
print(num2)
num2.pop(2) #elimina o valor na posição 2
print(num2)
num2.remove(2) #remove o valor da lista - somente o primeiro valor
print(num2)
#laço para utilizar remove
if 4 in num2:
    num2.remove(4)
else:
    print("Dont exist value 4.")
print(num2)
if 5 in num2:
    num2.remove(5)
else:
    print("Dont exist value 4.")
print(num2)
print('\n')
print('\n')
valores =[]
valores.append(5)
valores.append(4)
valores.append(9)
print(valores)
for v in valores:
    print(f'{v}...', end='')
print('\n')
for c, v in enumerate(valores):
    print(f'Na posição {c}, o valor é {v}')
"""
values = []
for cont in range(0, 5):
    values.append(int(input('Digit a number[0 - 9]:')))
print(values)
print('\n')
"""
a = [2, 3, 5, 7]
b = a
print(f'Lista {a}')
print(f'Lista {b}')
print('\n')
a = [2, 3, 5, 7]
b = a
b[2] = 8 #se igualar a lista, as mudanças vão para as duas tuplas
print(f'Lista {a}')
print(f'Lista {b}')
print('\n')
a = [2, 3, 5, 7]
b = a[:] #aqui só foi copiada a lista, nã foi igualada  
b[2] = 8 
print(f'Lista {a}')
print(f'Lista {b}')