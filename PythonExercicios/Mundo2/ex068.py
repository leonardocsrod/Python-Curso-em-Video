'''To create game odds or evens'''
from random import randint
print('=-' * 12)
print('Lets play odd or even!!!')
print('=-' * 12)
winPlayer1 = 0
winComputer = 0 
result1 = ''
result2 = ''
while True:
    player1 = int(input('Say a number: '))
    computer = randint(0, 10)
    total = player1 + computer    
    choicePlayer1 = ' '
#Odd or even logic
    while choicePlayer1 not in 'eo':
        choicePlayer1 = str(input('odd or even: ')).strip().lower()[0]
    print(f'You played {player1} and the computer played {computer}. The total was {total}.')
    if (total % 2) == 0 and choicePlayer1 == 'o':
        winPlayer1 += 1
        print('It\'s odd')
        print('You win.')
    elif (total % 2) == 0 and choicePlayer1 == 'e':
        print('It\'s odd')
        print('You lose.')
        break
    elif (total % 2) != 0 and choicePlayer1 == 'o':
        print('It\'s even')
        print('You lose.')
        break
    elif (total % 2) != 0 and choicePlayer1 == 'e':
        winPlayer1 += 1
        print('It\'s even')
        print('You win.')
    print('Let\'s play again...')
print(f'Game over! You win {winPlayer1} times!')     
