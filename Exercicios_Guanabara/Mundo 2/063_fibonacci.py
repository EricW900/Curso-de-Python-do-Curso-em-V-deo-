#Este código mostra os n termos de uma sequência de Fibonacci.
#Eric Peneres Carneiro#

n = int (input ('Insira aqui o termo da sequência: '))
n1 = 0
n2 = 1
cont = 0

while cont < n:
    print (n1, end = ' ')
    nt = n1 + n2
    n1 = n2
    n2 = nt
    cont += 1
print ('\nFim da sequência de Fibonacci.')    