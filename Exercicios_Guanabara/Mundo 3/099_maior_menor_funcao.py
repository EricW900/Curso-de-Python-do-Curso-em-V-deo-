#Este código cria uma função para contar o maior e menor número de uma lista
#Eric Peneres Carneiro#

from random import randint
from time import sleep


def preencher(lists):
    comprimentolista = randint (1, 10)
    for numeros in range(comprimentolista):
        lists.append(randint(1, 20))

    
def linhas():
    print('=' * 30)


def maior(list):
    print('Os valores dessa lista são', end=' ')
    for numeros in list:
        print(f'{numeros}', end=' ', flush=True)
        sleep(0.3)  
    print(f'e foram informados {len(list)} números!')
    print(f'O maior número é o {max(list)}!')


numeros = [4, 7, 2, 6, 3, 9]
numeros1 = [ ]
numeros2 = []
numeros3 = []
numeros4 = []
numeros5 = []

preencher(numeros1)
preencher(numeros2)
preencher(numeros3)
preencher(numeros4)
preencher(numeros5)

linhas()
maior(numeros)
linhas()
maior(numeros1)
linhas()
maior(numeros2)
linhas()
maior(numeros3)
linhas()
maior(numeros4)
linhas()
maior(numeros5)
linhas()
