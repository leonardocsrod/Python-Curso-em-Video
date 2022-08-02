list = []
expression = str(input("Digit a expression: "))
for simb in expression:
    if simb == '(':
        list.append('(')
    elif simb == ')':
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
            break
if len(list) == 0:
    print('Your expression is valid!')
else:
    print('Your expression is not valid!')
print(f'Digited expression: {expression}')
