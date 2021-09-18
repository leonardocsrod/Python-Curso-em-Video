speedcar = int(input('Speed car: '))
if speedcar <= 80:
    print('It´s ok, have a good trip!')
else:
    trafficticket = (speedcar - 80) * 7
    print('Speeding! Traffic ticket: R$ {:.2f}'.format(trafficticket))
    print('Have a nice day. Drive safety!')
