print('==========LELÉO LOJAS=========')
total_price = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
option = int(input('Choose an option: '))

if option == 1:
    final_price = total_price * 0.9
    print('Your purchase price is R${:.2f}.'.format(final_price))
elif option == 2:
    final_price = total_price * 0.95
    print('Your purchase price is R${:.2f}.'.format(final_price))
elif option == 3:
    final_price = total_price /2
    print('Your purchase price is 2 x R${:.2f}.'.format(final_price))
elif option == 4:
    portion = int(input('How many portions [3x or more]: ')) 
    final_price = (total_price * 1.2) / portion
    print('Your purchase price is {} x de R$ {:.2f}.'.format(portion, final_price)) 
