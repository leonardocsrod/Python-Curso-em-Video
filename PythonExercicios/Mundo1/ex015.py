days = int(input('How many days: '))
km = int(input('How many KMs: '))
total = (60 * days) + (0.15 * km)
print("The total to pay is: R${:.2f}.".format(total))