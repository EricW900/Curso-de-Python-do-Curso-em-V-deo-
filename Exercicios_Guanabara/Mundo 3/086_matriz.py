#Este código mostra uma matriz montada pelo usuário.
#Eric Peneres Carneiro#

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int (input (f'Insira um número para a linha {l} e posição {c}: '))

print (matriz[0])
print (matriz[1])
print (matriz[2])