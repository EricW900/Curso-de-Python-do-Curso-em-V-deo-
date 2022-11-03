#Este código calcula o aumento salárial de um funcionário
#Eric Peneres Carneiro#

s = float (input ('Insira aqui o seu salário: '))

if s > 1250.00:
    print ('Seu salário foi aumentado em 10% e agora está no valor de R${:.2f}'.format (s * 1.10 ))
else:
    print ('Seu salário foi aumentado em 15% e agora está no valor de R${:.2f}'.format (s * 1.15))    