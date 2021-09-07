# \033[0:33:44m - estilo/text/fundo
# 0, 1, 4, 7 estilo
# 30 a 37 - cor do texto
# 40 a 47 - cores de fundo
# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[m
# \033[7;30m
name = 'Hello word!'
print('{}'.format(name))
print('{}{}{}'.format('\033[0;30;41m', name, '\033[m'))
print('\033[4;33;44m{}\033[m'.format(name))
print('\033[1;35;43m{}\033[m'.format(name))
print('\033[30;42m{}\033[m'.format(name))
print('\033[m{}\033[m'.format(name))
print('\033[7;40m{}\033[m'.format(name))
