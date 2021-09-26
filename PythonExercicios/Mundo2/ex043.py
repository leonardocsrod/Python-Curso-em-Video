weight = float(input('Inform your weight: '))
height = float(input('Inform your height: '))
imc = weight / (height ** 2)
if imc < 18.5:
    print('Your IMC (\033[1;31;40m{:.2f}\033[m) is \033[1;31;40munder weight\033[m.'.format(imc))
elif imc <= 25:
    print('Your IMC (\033[1;31;40m{:.2f}\033[m) is \033[1;31;40mideal weight\033[m.'.format(imc))
elif imc <= 30:
    print('Your IMC (\033[1;31;40m{:.2f}\033[m) is \033[1;31;40moverweight\033[m.'.format(imc))
elif imc <= 40:
    print('Your IMC (\033[1;31;40m{:.2f}\033[m) is \033[1;31;40mobesity\033[m.'.format(imc))
else:
    print('Your IMC (\033[1;31;40m{:.2f}\033[m) is \033[1;31;40mmorbid obesity\033[m.'.format(imc))