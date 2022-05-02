extendedInFull = ('zero', 'one', 'two', 'three', 'four', 'five', 'six',
'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
'fiveteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
choice = int(input("Digit a number between 0 and 20: "))
ender = 'n'
while choice < 0 or choice > 20:
    print('The number is not valid: ')
    choice = int(input("Digit a number between 0 and 20: "))

print(f'You digit the number: {extendedInFull[choice]}')
