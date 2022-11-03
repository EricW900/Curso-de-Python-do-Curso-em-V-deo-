#Este código mostra o maior e menor peso de cinco pessoas.
#Eric Peneres Carneiro#

lp = []
for i in range (1, 5+1):
    p = float (input ('Insira aqui o peso da pessoa: Kg'))
    lp.append(p)
print ('O maior peso é {}Kg e o menor peso é {}Kg.'.format(max(lp), min(lp)))
     