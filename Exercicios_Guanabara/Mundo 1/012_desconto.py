#Este código calcula 5% de desconto sobre o preço de um produto.
#Eric Peneres Carneiro# 

p = float (input ('Insira aqui o preço do produto a ser descontado R$ '))
print ('O valor de R${} com desconto de 5% é de R${}'.format(p, p - (p * 5/100)))