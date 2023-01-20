
estatisticas = []
jogadores = {}
jogadoresfinal = {}
golsp = []

res = 'S'


while res == 'S':
    jogadores["Nome"] = str (input ('Insira o nome do jogador: ')).capitalize()
    qtdp = int (input (f'Insira a quantidade de partidas que o {jogadores["Nome"]} jogou: '))

    for partidas in range (qtdp):
        gols = int (input (f'Quantidade de gols na {partidas+1}° partida: ').strip())
        golsp.append(gols)
        jogadores["Gols por partida"] = golsp[:]
    jogadores["Total de gols"] = sum(golsp)
    jogadoresfinal = jogadores.copy()
    jogadores.clear()    
    estatisticas.append(jogadoresfinal)
    golsp.clear()

    res = str (input ('Quer continuar? [S/N]')).upper() 
    if res == 'N':
        break   

for jogador in estatisticas:
    print (f'O jogador {jogador["Nome"]} marcou por partida {jogador["Gols por partida"]}', end = ' ')
    print (f'O total de gols foi {jogador["Total de gols"]}')
   
