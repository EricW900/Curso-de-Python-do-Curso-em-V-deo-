#Este código mostra qual número é o maior ou o menor
#Eric Peneres Carneiro#

n1 = int (input ('Insira aqui o primeiro número: '))
n2 = int (input ('Insira aqui o segundo número: '))
n3 = int (input ('Insira aqui o terceiro número: '))

if n1 > n2 and n1 > n3:
    print (f'O número {n1} é o maior número.')
if n2 > n1 and n2 > n3:
    print (f'O número {n2} é o maior número.')
if n3 > n1 and n3 > n2:
    print (f'O número {n3} é o maior número.')

if n1 < n2 and n1 < n3:
    print (f'O número {n1} é o menor número.')
if n2 < n1 and n2 < n3:
    print (f'O número {n2} é o menor número.')
if n3 < n1 and n3 < n2:
    print (f'O número {n3} é o menor número.')