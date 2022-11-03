#Este código calcula uma progressão aritmética.
#Eric Peneres Carneiro#

prt = int (input ('Insira o primeiro termo da razão: '))
r = int (input ('Insira a razão da progressão aritmética: '))
e = prt + (10 - 1) * r

for a in range (prt, e+1, r):
    print (a)  