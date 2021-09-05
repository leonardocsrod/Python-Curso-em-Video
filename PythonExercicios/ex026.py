phrase = str(input('Digit a phrase: ')).strip().lower()
print('The letter A shows {} times in phrase.'.format(phrase.count('a')))
print('The first letter A appeared on position {}'.format(phrase.find('a')+1))
print('The last letter A appeared on position {}'.format(phrase.rfind('a')+1))
