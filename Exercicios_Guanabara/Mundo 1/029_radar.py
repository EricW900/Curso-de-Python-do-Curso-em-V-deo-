#Este código calcula a multa de um radar
#Eric Peneres Carneiro#

v = int (input ('Insira a velocidade do veículo: '))
if v > 80:
    print ('O veículo ultrapassou o limite de velocidade de 80km/h e foi multado em R${}!'.format((v - 80) * 7))
else:
    print ('O veículo estava dentro do limite de velocidade!')   