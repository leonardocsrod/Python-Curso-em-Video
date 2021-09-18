salary = float(input('Inform your salary: '))
if salary <= 1250:
    salary =  salary * 1.15;
else:
    salary = salary * 1.1;

print('Your new salary is \033[0;31;44m{:.2f}\033[m'.format(salary)) 