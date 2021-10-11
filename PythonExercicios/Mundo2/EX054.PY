import datetime
hoje = datetime.date.today().year
count_minusage = 0
count_moreage = 0
for c in range(1, 8):
    age = int(input('What a year the {}º person borned: '.format(c)))
    if (hoje - age < 18):
        count_minusage += 1
    else:
        count_moreage += 1
print('we have {} people legal age and {} people not legal age!'.format(count_moreage, count_minusage))
