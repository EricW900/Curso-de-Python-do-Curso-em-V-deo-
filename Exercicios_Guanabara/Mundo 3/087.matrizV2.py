#Este código é um aprimoramento da primeira matriz feita no exercício anterior.
#Eric Peneres Carneiro#

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = []
lista = []

for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int (input ('Insira um número: '))

print ('-=-' * 20)        

print (matriz[0])
print (matriz[1])
print (matriz[2])

print ('-=-' * 20)

for n in matriz[0]:
    if n % 2 == 0:      
       lista.append(n)
       
for n in matriz[1]:
    if n % 2 == 0:
        lista.append(n)

for n in matriz[2]:
    if n % 2 == 0:
        lista.append(n)

soma.append(matriz[0][2])
soma.append(matriz[1][2])
soma.append(matriz[2][2])      

print (f'A soma de todos os números pares é {sum(lista)}')
print (f'A soma dos valores da terceira coluna é {sum(soma)}')  
print (f'O maior valor da segunda linha é {max(matriz[1])}')
    