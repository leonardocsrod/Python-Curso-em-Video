phrase = str(input('Write a phrase: ')).strip().upper()
words = phrase.split()
together = ''.join(words)
inverse = ''

for c in range(len(together) - 1, -1, -1):
    inverse += together[c]
if inverse == together:
    print('THE PHRASE IS A PALINDROMO!')
else:
    print('THE PHRASE ISN´T A PALINDROMO!')

print(together, inverse)
