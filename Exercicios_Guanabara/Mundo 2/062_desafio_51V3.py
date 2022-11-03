#Este código é uma versão ainda mais melhorada do desafio anterior.
#Eric Peneres Carneiro#


prt = int (input ('Insira aqui o primeiro termo: '))
r = int (input ('Insira aqui a razão da progressão aritmética: '))
t = prt
contador = 1
ef = 10
tot = 0

while ef != 0:
    tot = tot + ef
    while contador <= tot:
        print (t)
        t += r
        contador += 1
    ef = int (input ('Quantos números a mais você quer adicionar? '))    
print ('Progressão Finalizada!')