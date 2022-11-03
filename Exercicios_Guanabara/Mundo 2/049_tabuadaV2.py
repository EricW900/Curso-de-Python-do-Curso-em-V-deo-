#Este código imprimi uma tabuada inserida pelo usuário.
#Eric Peneres Carneiro#

n = int (input ('Insira aqui o número que você quer ver a tabuada: '))
for t in range (1, 10+1):    
    print ('{} x {:2} = {}'.format(n, t, t*n))        