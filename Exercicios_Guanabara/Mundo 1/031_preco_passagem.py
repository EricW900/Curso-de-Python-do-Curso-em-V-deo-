#Este código calcula o preço de uma passagem
#Eric Peneres Carneiro#

km = float (input ('Insira aqui a quantidade de Kms que você irá viajar: '))
if km <= 200:
    print ('Você irá pagar RS{:.2f}.'.format (km * 0.50))
else:
    print ('Você irá pagar RS{:.2f}.'.format (km * 0.45))   