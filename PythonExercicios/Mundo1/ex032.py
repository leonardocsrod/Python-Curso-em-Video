import datetime
year0 = int(input('Digit the year: '))
if year0 == 0:
    year0 = datetime.date.today().year
if year0 % 4 == 0 and year0 % 400 == 0 or year0 % 100 != 0:
    print('The year \033[0;30;44m{}\033[m is bissextile!'.format(year0))
else:
    print('The year \033[0;30;44m{}\033[m is not bissextile!'.format(year0))
