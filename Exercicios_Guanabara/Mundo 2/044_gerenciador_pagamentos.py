#Este código simula um gerenciador de pagamentos.
#Eric Peneres Carneiro#

p = float (input ('Insira aqui o valo do produto a ser pago: R$'))
pgt = int (input ('Insira aqui a forma de pagamento (1 = À vista no dinheiro ou cheque, 2 = À vista no cartão, 3 = 2x no cartão e 4 = 3x ou mais no cartão): '))

if pgt == 1:
    pf = p - (p * 10/100)
    print ('Você escolheu pagar à vista no dinheiro ou cheque e irá ganhar um desconto de 10%!')
    print ('Agora você irá pagar R${:.2f} no produto.'.format(pf))
elif pgt == 2:
    pf = p - (p * 5 / 100)
    print (r'Você escolheu pagar à vista no cartão e ganhou 5% de desconto!')
    print ('Agora você irá pagar R${:.2f} no produto.'.format(pf))
elif pgt == 3:
    pf = p / 2
    print ('Você escolheu pagar em 2x no cartão.')
    print ('Você irá pagar R${} por mês no produto'.format(pf))
elif pgt == 4:
    pa = int (input ('Quantas parcelas você irá pagar?: '))
    pi = p + (p * 20 / 100)
    pf = pi / pa
    print ('Você escolheu pagar parcelado em mais de 3x no cartão.')
    print ('Você irá pagar {} parcelas de R${:.2f} no produto e o preço final será de R${}.'.format(pa, pf, pi))