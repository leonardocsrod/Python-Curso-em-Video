name = input('What is your name: ').strip().lower()
if name == 'leonardo':
    print('what a beautiful name, {}.'.format(name))
elif name == 'pedro' or name == 'maria':
    print('{} is very popular in Brazil'.format(name))
elif name in 'ana claudia jessica':
    print('Beautiful female name {}'.format(name))
else:
    print('Your name is so normal {}!'.format(name))    
print('Have a nice day {}!'.format(name))
