first_grade = float(input('First grade: '))
second_grade = float(input('Second grade: '))
average = (first_grade + second_grade) / 2

if average < 5:
    print('Your average is \033[1;31;40m{:.2f}\033[m, You are disapproved!'.format(average))
elif average >= 5 and average < 7:
    print('Becareful, Your average is \033[1;33;40m{:.2f}\033[m, You are recovering!'.format(average))
else:
    print('Congratulations!!! \nYour average is \033[1;34;40m{:.2f}\033[m, You are approved!'.format(average))