import random
name1 = str(input('Student 1: '))
name2 = str(input('Student 2: '))
name3 = str(input('Student 3: '))
name4 = str(input('Student 4: '))

list = [name1, name2, name3, name4];
listchoosed = random.choice(list)
print("The chooses student is: {} ".format(listchoosed))

