age_older = 0
counter_woman = 0
average = 0
for c in range(1, 5):
    name = str(input('Name: '))
    age = int(input('Age: '))
    average += age 
    sex = str(input('Gender[m/f]: ')).lower()
    if c ==1 and sex == 'm':
        name_older = name
        age_older = age
    if sex == 'm' and age > age_older:
        name_older = name
        age_older = age        
    if sex == 'f' and age <= 20:
        counter_woman += 1
average /= 4
print('The age average is {}.'.format(average))
print('The oldest man has {} years and call yourself {}'.format(age_older, name_older))
print('There is {} women lower 20 years.'.format(counter_woman))