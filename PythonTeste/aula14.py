#laços

print('With \033[33mfor\033[m')

for c in range(1,11):
    print(c)
print('The end\n')

print('With \033[33mwhile\033[m')
c = 1
while(c < 11):
    print(c)
    c += 1
print('The end')
