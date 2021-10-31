sex = str(input('Inform your gender: ')).upper().strip()[0]
while sex not in 'MmFf':
    sex = str(input('Invalid data, please, inform your gender: ')).upper().strip()[0]
print('Gender \'{}\' registered with sucess!'.format(sex)) 