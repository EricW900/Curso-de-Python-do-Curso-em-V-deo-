#Este código gera palpites de acordo com as regras do exercício 88. 
#Eric Peneres Carneiro#

from random import randint
from time import sleep

l = []
lf = []
excesso = []

print ('-=' * 20)
palpites = int (input ('Insira a quantidade de palpites: '))
print (f'Os {palpites} palpites foram gerados!')
print ('-=' * 20)

while palpites >= 0:
    for n in range (0, 6):
        num = randint(1, 61)
        if num in l:
            excesso.append(num)
        l.append(num)        
    lf.append(l[:])
    l.clear()    
    palpites -= 1
    if palpites == 0:
        break

for a in range (len(lf)):
    sleep(1)
    print (f'Jogo: {a} {sorted(lf[a])}') 
print ('-=' * 20)
print ('BOA SORTE!')
