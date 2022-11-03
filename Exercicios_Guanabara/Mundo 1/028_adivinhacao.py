#Este código é um jogo de adivinhação de números
#Eric Peneres Carneiro#

from random import randint

n = randint(1, 5)
print ('Vamos descobrir um número?')
nn = int (input ('Insira aqui um número de 1 a 5 e o computador irá dizer se é o número certo ou não: '))
print (f'O número inserido foi {nn} e o número sorteado foi {n}')
print ('Número correto'if nn == n else 'Número incorreto')