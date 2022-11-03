#Este código calcula a hipotenusa de um triângulo retângulo
#Eric Peneres Carneiro# 

from math import hypot

co = float (input ('Insira o cateto oposto: '))
ca = float (input ('Insira o cateto adjacente: '))
print ('O valor da hipotenusa é {:.2f}.'.format(hypot(co, ca)))