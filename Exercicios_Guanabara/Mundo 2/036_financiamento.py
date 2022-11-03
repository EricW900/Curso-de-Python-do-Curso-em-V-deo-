#Este código simula o financimento de uma casa.
#Eric Peneres Carneiro#

#Perguntar valor da casa, salário e quantidade de parcelas.
#Calcular valo da prestação mensal, não pode exceder 30% do salário.
 
v = float (input ('Insira o valor da casa: '))
s = float (input ('Insira o valor do seu salário: '))
p = int (input ('Insira a quantidade de anos que você quer pagar: '))

a = p * 12
vp = v / a
if vp > s * 0.3:
    print ('O financiamento não foi aprovado.')
else:
    print ('O financiamento foi aprovado, você irá pagar a casa em {} anos, e em {} parcelas de R${:.2f}.'.format (p, a, vp))