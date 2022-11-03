#Este código usa o while para gerar uma progressão aritmética.
#Eric Peneres Carneiro#

prt = int (input ('Insira o primeiro termo da razão: '))
r = int (input ('Insira a razão da progressão aritmética: '))

t = prt
cont = 1

while cont <= 10:
    print (t)
    t += r
    cont += 1    