#Este código calcula a área de um terreno com funções.
#Eric Peneres Carneiro#


def inicio(msg):
    print('-' * 15)
    print(msg)
    print('-' * 15)


def valores(l, c):
    calculoarea = l * c
    print(f'A área de um terreno {l}x{c} é de {calculoarea}m.')


l = float (input ('Insira a largura do terreno: '))
c = float (input ('Insira o comprimento do terreno: '))

inicio('Controle de terrenos')
valores(l, c)