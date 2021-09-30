"""""
/for c in range(0, 3):
    print('Oi')
print('Fim\n')

for c in range(0, 3):
    print(c)
print('Fim\n')

for c in range(6, -1, -1):
    print(c)
print('Fim\n')

number = int(input("Digit a number: "))
for c in range(0, number):
    print(c)
print('Fim\n')

number = int(input("Digit a number: "))
for c in range(0, number + 1):
    print(c)
print('Fim\n')

begin = int(input('Begin: '))
end = int(input("End: "))
step = int(input("Step: "))

for c in range(begin, end + 1, step):
    print(c)
print('The End\n')
"""

sum = 0
for c in range(0, 10):
    number = int(input("Digit a number: "))
    sum = sum + number
    #sum += number
print(sum)
