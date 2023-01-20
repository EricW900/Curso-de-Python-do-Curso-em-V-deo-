#Este código adiciona números em uma lista e os imprime em ordem crescente sem utilizar a função sort. 
#Eric Peneres Carneiro#

lista = []

for c in range (0, 5):
    numero = int (input ('Insira um número para colocar na lista: '))
    if c == 0 or c > lista[-1]:
        lista.append(numero)
    else:
        p = 0
        while p < len(lista):
            if numero <= lista[p]:
                lista.insert(p, numero)
                break
print (f'A lista inserida foi {lista}')            