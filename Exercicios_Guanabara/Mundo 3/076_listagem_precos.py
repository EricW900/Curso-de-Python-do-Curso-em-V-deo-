


t = ('Pao', 3, 'Carne', 5, 'Bolacha', 7, 'Mortadela', 8, 'Bala de Goma', 1)

print ('-=-' * 10)
print ('LISTAGEM DE PREÇOS')
print ('-=-' * 10)

for p in range (len(t)):
    if p % 2 == 0:
        print (f'{t[p]:.<15}', end = ' ')
    else:
        print (f'R${t[p]:>2.2f}')
