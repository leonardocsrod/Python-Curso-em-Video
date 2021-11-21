import random
computer = random.randint(0, 10)
print('Let\'s play. I choose a number between 1 to 10, you try to guess it.')
you = 11
counter = 0
while computer != you:
    you = int(input('What\'s your number: '))
    counter += 1
    if you < computer:
        print('It\'s low, try again! ')
    else:
        print('It\'s high, try again!')
print('Congratulations, your number {} is right!'.format(you))
print('My number is {}.'.format(computer))
print('You tryed {} times.'.format(counter))    