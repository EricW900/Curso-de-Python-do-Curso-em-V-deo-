#Este código mostra quantas vogais tem em uma tupla.
#Eric Peneres Carneiro#

p = ('Teste', 'Auto', 'Carta', 'Intensivo', 'Brando')
cont = 0

for i in p:
    print (f'\nNa palavra {i} tem: ')
    for l in i:
        if l in 'aeiou':
            print (l, end = ' ')