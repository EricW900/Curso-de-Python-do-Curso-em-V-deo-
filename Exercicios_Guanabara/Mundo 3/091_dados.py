#Este código simula um jogo de dados de acordo com o exercício 91. 
#Eric Peneres Carneiro#

from random import randint
from time import sleep

ordem = {}

jogadores = {"Jogador 1" : randint(1, 6),
             "Jogador 2" : randint (1, 6),
             "Jogador 3" : randint (1, 6),
             "Jogador 4" : randint (1, 6) }

for k, v in jogadores.items():
    print (f'O jogador {k} jogou o valor {v} do dado.')
    sleep(1)

ordem = sorted(jogadores.items(), key=lambda item: item[1], reverse = True)

print ('=' * 20)
for n in enumerate(ordem):
    print (f'{n[0]+1}° lugar: {n[1][0]}')
    sleep(1)