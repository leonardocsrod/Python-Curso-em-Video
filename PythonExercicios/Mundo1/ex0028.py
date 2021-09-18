import random
import time
computernumber = random.randint(1, 5)
print('-=-' * 15)
yournumber = int(input('Choose a number between 1 to 5: '))
print('PROCESSANDO...')
time.sleep(3) #atraso de 3 segundo

if computernumber == yournumber:
    print('Congratulations! You win!')
else:
    print('You lost')
print('-=-' * 15)