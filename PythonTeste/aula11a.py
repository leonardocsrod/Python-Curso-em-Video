# \033[0:33:44m - estilo/text/fundo
# style - 0 none, 1 bold, 4 underline, 7 negative
# text color - 30 white, 31 red, 32 green, 33 yellow, 34 blue, 35 purple, 36 light blue, 37 grey
# background color - 40 white, 41 red, 42 green, 43 yellow, 44 blue, 45 purple, 46 light blue, 47 grey

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
