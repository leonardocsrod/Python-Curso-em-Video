number1 = int(input("First number: "))
number2 = int(input("Second number: "))
if number1 > number2:
    print("First number (\033[1;31;40m{}\033[m) is bigger!".format(number1))
elif number2 > number1:
    print("Second number (\033[1;31;40m{}\033[m) is bigger!".format(number2))
elif number1 == number2:
    print("The numbers (\033[1;31;40m{}\033[m) and (\033[1;31;40m{}\033[m) are equals!".format(number1, number2))
    