import datetime
birth_year = int(input("Inform your birth year: "))
age = datetime.date.today().year - birth_year
print('Year of birth: \033[1;34;35m{}\033[m'.format(birth_year))
print('The athlete is \033[1;34;35m{}\033[m years old.'.format(age))
if age < 9:
    print('Classification: \033[1;34;35mMirim\033[m')
elif age < 14:
    print('Classification: \033[1;34;35mInfantil\033[m')
elif age < 19:
    print('Classification: \033[1;34;35mJunior\033[m')
elif age < 25:
    print('Classification: \033[1;34;35mSenior\033[m')
else:
    print('Classification: \033[1;34;35mMaster\033[m')