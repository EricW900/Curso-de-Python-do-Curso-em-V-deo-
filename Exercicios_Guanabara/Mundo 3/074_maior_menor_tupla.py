#Este código gera uma tupla com 5 números e mostra o maior e menor valo gerado.
#Eric Peneres Carneiro#

from random import randint

l = (randint (1, 999), randint (1, 999), randint (1, 999), randint (1, 999), randint (1, 999))

mav = max(l)
mev = min(l)

print (l)
print (f'O maior valor é {mav}')
print (f'O menor valor é {mev}')