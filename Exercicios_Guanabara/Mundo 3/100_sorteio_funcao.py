#Este código cria um sistema de sorteio utilizando funções
#Eric Peneres Carneiro#


from random import randint
from time import sleep

def sorteio(list):
    excesso = []
    for numeros in range (1, 6):
        n = randint(1, 60)
        if n in list:
            excesso.append(n)
            list.append(randint(1, 60))
        else:
            if n not in list:
                list.append(n)

    print ('Os números sorteados foram: ')
    for numeros in list:
        sleep(0.3)
        print (f'{numeros}', end=' ', flush=True)


def somarpars(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)   
    print (f'A soma dos valores pares foi: {sum(pares)}')

listasorteio = []

sorteio(listasorteio)
print (' ')
somarpars(listasorteio)
