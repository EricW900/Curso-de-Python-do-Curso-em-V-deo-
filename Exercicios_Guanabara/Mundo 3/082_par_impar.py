#Este código irá ler números para compor listas de números pares e impares e após isso mostra o conteúdo delas.
#Eric Peneres Carneiro#

from random import randint

lp = []
li = []
l = []
es = 'S'

while True:    
    v = int (input ('Insira aqui um valor: '))    
    l.append(v)        
    if v % 2 == 0:
        lp.append(v)
    else:
        li.append(v)
    e = str (input ('Quer continuar? [S/N] ')).upper().strip()    
    if e != es:
        break                  
    
print ('-=-' * 30)
print ('LISTA DE NÚMEROS PARES')
print ('-=-' * 30)
print (lp)
print ('-=-' * 30)
print ('LISTA DE NÚMEROS IMPARES')
print ('-=-' * 30)
print (li)
print ('-=-' * 30)
print ('LISTA DE NÚMEROS')
print ('-=-' * 30)
print (l)
    