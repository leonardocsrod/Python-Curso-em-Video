words = ('aprender', 'programar', 'linguagem', 'python',
'curso', 'grátis', 'estudar', 'praticar', 'trabalhar', 'mercador',
'programador', 'futuro')

for i in words:
    print(f'In word \033[1;32;40m{i}\033[m, we have ', end='')
    for word in i:
        if word.lower() in 'aeiou':
            print(f'\033[1;32;40m{word}\033[m', end=' ')
    print('\n')
