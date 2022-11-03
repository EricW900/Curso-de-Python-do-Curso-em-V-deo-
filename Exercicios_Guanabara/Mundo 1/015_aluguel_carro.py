#Este código calcula o preço de um serviço de aluguel de carros.
#Eric Peneres Carneiro#

dia = int (input ('Quantos dias você alugou esse carro?: '))
km = float (input ('Quantos Kms você rodou com esse carro?: '))
print ('Você irá pagar R${:.2f}'.format (dia * 60 + km * 0.15))