#Este código calcula um triângulo baseado no exercício 42 do curso de Python. 
#Eric Peneres Carneiro#

r1 = float (input ('Insira aqui o comprimento da primeira reta do triângulo: '))
r2 = float (input ('Insira aqui o comprimento da segunda reta do triângulo: '))
r3 = float (input ('Insira aqui o comprimento da terceira reta do triângulo: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print ('Os valores formam um triângulo')   

    if r1 == r2 == r3:
        print ('Os valores formam um triângulo equilátero.')

    elif r1 == r2 or r2 == r3 or r3 == r2 or r3 == r1:
        print ('Os valores formam um triângulo Isósceles.')

    elif r1 != r2 != r3:
        print ('Os valores formam um triângulo Escaleno.')
else:
    print ('Os valores não formam um triângulo')     