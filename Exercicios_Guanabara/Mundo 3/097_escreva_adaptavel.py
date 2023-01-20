#Este código mostra uma palavra adaptável com linhas em cima e baixo.
#Eric Peneres Carneiro#

def escreva(mensg):
    tam = len(mensg) + 4
    print('-' * tam)
    print(f'  {mensg}')
    print('-' * tam)


escreva('Olá, isso é um teste!')
escreva('Opala 1978!')
escreva('Chevette de drift com kit angulo!')
