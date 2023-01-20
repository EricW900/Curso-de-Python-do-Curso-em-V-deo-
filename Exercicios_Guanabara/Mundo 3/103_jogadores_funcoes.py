#Este código nos apresenta utilizando funções a ficha de um jogador.
#Eric Peneres Carneiro#

def jogador(nome = ' ', gols = 0):
    if nome.strip() == '' and gols == 0:
        print (f'O jogador que não existe marcou nenhum gol!')
    elif gols == 0:
        print (f'O jogador {nome} marcou nenhum gol!')
    elif nome.strip() == '':
        print (f'O jogador que não tem nome marcou {gols} gols!')
    else:
        print (f'O jogador {nome} marcou {gols} gols!')

gols = None

nome = str (input ('Insira o nome do jogador: '))
gols = str (input ('Insira a quantidade de gols do jogador: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

jogador(nome, gols)
