#Este código imprime uma análise da tabela do Campeonato Brasileiro de Futebol.
#Código feito com base na rodada 35 do Brasileirão e da tabela do dia 03/11/2022
#Eric Peneres Carneiro#

from random import choice

tabela = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico - Pr',
'Atlético - MG', 'São Paulo', 'América - MG', 'Fortaleza', 'Botafogo', 'Santos', 'Bragantino', 'Goiás',
'Coritiba', 'Cuiabá', 'Ceará', 'Atlético - GO', 'Avaí', 'Juventude')

print ('-=-' * 30)
print (f'Os cinco primeiros colocados do Brasileirão 2022 são {tabela[:6]}')
print (f'Os últimos quatro colocados do Brasileirão 2022 são {tabela[16:]}')
print ('-=-' * 30)
print (sorted(tabela))
print ('-=-' * 30)
t = choice(tabela)
print ('-=-' * 30)
print (f'O {t} está localizado na posição {tabela.index(t)+1}')