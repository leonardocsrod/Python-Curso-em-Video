''' TUPLAS'''
lanche = ('Hamburguer', 'Suco', 'Pizza','Pudim')
'''print(f'Tupla lanche = {lanche}')
print(f'lanche[1] = {lanche[1]}')
print(f'lanche[-2] = {lanche[-2]}')
print(f'lanche[1:3] = {lanche[1:3]}')
print(f'lanche[2:] = {lanche[2:]}')
print(f'lanche[:2] = {lanche[:2]}')
print(f'lanche[-2] = {lanche[-2]}')
print(f'lanche[-2:] = {lanche[-2:]}')
#lanche[1] = 'refri' -> tuplas são imutáveis
for c in lanche:
    print(f'I\'m going to eat {c}')
#print(len(lanche))
for cont in range(0, len(lanche)):
    print(f'I\'m going to eat {lanche[cont]}')
 for position, comida in enumerate(lanche):
    print(f'I\'m going to eat {comida} in position {position}.')
print(lanche)
print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(f'Tupla a = {a}')
print(f'Tupla b= {b}')
print(f'Tupla c = {c}')
print(f'Tupla d = {d}')
print(f'sorted c = {sorted(c)}') #põe em ordem
print(f'sorted d = {sorted(d)}')
print(f'len(c) = {len(c)} elementos')#conta os elementos da tupla
print(f'c.count(5) = {c.count(5)} elementos')#conta o item no parêntese
print(f'c.index(8) = {c.index(8)}')#mostra em que posição está o item no parêntese
print(f'c.index(2, 4) = {c.index(2, 4)}')#posição do item a partir do segundo item do parêntese'''
pessoa =  ('Gustavo', 39, 'm', 99.88)
print(pessoa)
del(pessoa)
print(pessoa) 
