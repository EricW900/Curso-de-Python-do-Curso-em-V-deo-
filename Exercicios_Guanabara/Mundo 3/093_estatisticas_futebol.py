#Este código mostra as estatísticas de um jogador.
#Eric Peneres Carneiro#

estatistica = {}
golsp = []

print ('-' * 20)

estatistica["Nome"] = str (input ('Insira o nome do jogador: ')).upper()
qtdp = int (input (f'Insira a quantidade de partidas que o {estatistica["Nome"]} jogou: '))

for partidas in range(qtdp):
    gols = int (input (f'Quantos gols feitos na partida {partidas+1}? '))
    golsp.append(gols)
    estatistica["Gols por partida"] = golsp[:]
estatistica["Total de Gols"] = sum(golsp)

print ('-' * 20)

for d, v in estatistica.items():
    print (d, v)

print ('-' * 20)

for v, g in enumerate(estatistica['Gols por partida']):
    print (f'Na partida {v+1}, o {estatistica["Nome"]} fez {g} gols.')    
    