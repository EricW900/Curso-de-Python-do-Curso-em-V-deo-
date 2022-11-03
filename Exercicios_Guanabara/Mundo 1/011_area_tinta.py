#Este código calcula a quantidade de tinta necessária para pintar uma parede de dimensões especificadas pelo usuário.
#Eric Peneres Carneiro#

print ('=' * 10, 'Bem vindo' ,'=' * 10)
l = float (input ('Insira aqui a largura da parede a ser pintada: '))
al = float (input ('Insira a altura da parede a ser pintada: '))
a = l * al
t = a / 2
print ('A área da parede é de {}m² e a quantidade de tinta necessária a ser utilizada será de {} litros.'.format(a, t))