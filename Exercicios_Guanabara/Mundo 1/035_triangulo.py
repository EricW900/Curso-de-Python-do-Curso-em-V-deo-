#Este código calcula a medida de três retas de um triângulo e diz se elas podem formar um triângulo ou não
#Eric Peneres Carneiro#

r1 = float (input ('Insira aqui o comprimento da primeira reta do triângulo: '))
r2 = float (input ('Insira aqui o comprimento da segunda reta do triângulo: '))
r3 = float (input ('Insira aqui o comprimento da terceira reta do triângulo: '))

print ('As medidas formam um triângulo' if r1 + r2 > r3 else 'As medidas não formam um triângulo.')