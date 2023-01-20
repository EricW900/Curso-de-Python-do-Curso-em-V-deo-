#Este código mostra números pares e impares em listas de forma crescente.
#Eric Peneres Carneiro#

l = [[], []]
for i in range (1, 8):
    n = int (input ('Insira um número: '))
    if n % 2 == 0:
        l[0].append(n)
    elif n % 2 == 1:
        l[1].append(n)
        
print (f'A lista de números pares é {sorted(l[0])}')
print (f'A lista de números impares é {sorted(l[1])}')
