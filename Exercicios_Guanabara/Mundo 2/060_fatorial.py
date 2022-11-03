#Este código calcula o fatorial de um número inserido.
#Eric Peneres Carneiro#
l = []
f = int (input ('Insira aqui o número para vermos o seu fatorial: '))

c = f
i = f
fa = 1

while c > 0:        
    fa *= c
    c -= 1    
print ('O fatorial de {} é {}.'.format(f, fa))
    