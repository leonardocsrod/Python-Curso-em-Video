name = str(input('What´s your name? ')).strip().lower()
names = name.strip().lower()
if names == 'leonardo':
    print('Hello {}, how are you!'.format(name))
else: 
    print('Nice to meet you {}!'.format(name))
