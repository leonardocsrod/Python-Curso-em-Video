value = float(input('What the house value: '))
salary = float(input('What is your salary: '))
years = int(input('How many years you will pay: '))
installment = value / (years * 12)
limit = salary * 0.3
print('To pay a house of R$ {:.2f} in {} years'.format(value, years), end=', ')
print('the installment is R$ {:.2f}.'.format(installment))

if installment <= limit:
    print('Your loan is approved, the installment is \033[1;33;44mR$ {:.2f}\033[m.'.format(installment))
else:
    print('Your loan is not approved, the installment is\033[1;33;44mR$ {:.2f}\033[m'.format(installment))