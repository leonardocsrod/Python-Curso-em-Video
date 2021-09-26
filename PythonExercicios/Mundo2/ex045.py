import random
print('Your options: ')
print('[ 0 ] - PEDRA')
print('[ 1 ] - PAPEL')
print('[ 2 ] - TESOURA')

options = ('PEDRA', 'PAPEL', 'TESOURA')
computer = random.randint(0, 2)
your_option = int(input('What´s your option [ 0, 1, 2]: '))
print('JO')
print('KEN')
print('PO!!!')

if computer == your_option:
    print('-=' * 15)
    print('Computer played {} '.format(options[computer]))
    print('You played {}'.format(options[your_option]))
    print('-=' * 15)
    print('DRAW')  
else:
    if (computer == 0 and your_option == 1) or (computer == 1 and your_option == 2) or (computer == 2 and your_option == 0):
       print('-=' * 15)
       print('Computer played {} '.format(options[computer]))
       print('You played {}'.format(options[your_option]))
       print('-=' * 15)
       print('YOU WIN') 
    else:
       print('-=' * 15)
       print('Computer played {} '.format(options[computer]))
       print('You played {}'.format(options[your_option]))
       print('-=' * 15)
       print('YOU LOSE') 

