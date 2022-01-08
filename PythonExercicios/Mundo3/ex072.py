extendNumber = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fiveteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
choose = ' '
while True:
    choose = ' '
    number = 30
    while number < 0 or number > 20:
        number = int(input('Digit a number betwwen zero and twenty: '))
    print(f'The digited number was {extendNumber[number]}')
    while choose not in 'yn':
        choose = str(input('Do you want to continue[Y/N]: ')).strip().lower()
    if choose == 'n':
        break
print('The end')
