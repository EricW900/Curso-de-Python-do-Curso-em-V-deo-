#Este código calcula valores pares de uma lista.
#Eric Peneres Carneiro#

l = []
soma = 0
for c in range (1, 6+1):    
    n = int (input ('Insira aqui um número inteiro: '))    
    if n % 2 == 0:
        l.append(n)
        print (l)
        soma += n
print ('A soma dos números pares é {}.'.format(soma))
