firstvalue = int(input('Digit the firt value: '))
secondvalue = int(input('Digit the second value: '))
thirdvalue = int(input('Digit the third value: '))
bigger = 0
smaller = 0
if firstvalue > secondvalue and firstvalue > thirdvalue:
    bigger = firstvalue
if secondvalue > firstvalue and secondvalue > thirdvalue:
    bigger = secondvalue
if thirdvalue > firstvalue and thirdvalue > secondvalue:
    bigger = thirdvalue

if firstvalue < secondvalue and firstvalue < thirdvalue:
    smaller = firstvalue
if secondvalue < firstvalue and secondvalue < thirdvalue:
    smaller = secondvalue
if thirdvalue < firstvalue and thirdvalue < secondvalue:
    smaller = thirdvalue
print('Bigger value: \033[0;33;44m{}\033[m'.format(bigger))
print('Smaller value: \033[0;32;43m{}\033[m'.format(smaller))
