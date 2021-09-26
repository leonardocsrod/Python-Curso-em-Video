import datetime

birth_year = int(input('Inform your birth year: '))
age = datetime.date.today().year - birth_year
enlistment = birth_year + 18
if age < 18:
    print('Who birth in {} has {} years in {}.'.format(birth_year, age, datetime.date.today().year))
    print("The enlistment will be in {}".format(enlistment))
else:
    print('Who birth in {} has {} years in {}.'.format(birth_year, age, datetime.date.today().year))
    print("The enlistment was in {}".format(enlistment))