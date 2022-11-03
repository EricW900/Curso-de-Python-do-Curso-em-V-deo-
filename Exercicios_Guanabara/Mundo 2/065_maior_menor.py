#Este código calcula o maior, menor e a soma de valores inseridos pelo usuário.
#Eric Peneres Carneiro#

from statistics import mean

l = []
cont = 0
contv = 0
s = 'S'
n = int (input ('Insira aqui um valor: '))
e = str (input ('Quer continuar? [ S / N ]? ')).upper().strip()
l.append(n)

while e == s:
    cont += 1
    contv += 1    
    n = int (input ('Insira aqui outro: '))
    l.append(n)
    e = str (input ('Quer continuar? [ S / N ]? ')).upper().strip()
    m = (max(l))
    me = (min(l))
    media = mean(l)   
else:
    print ('Você escolheu finalizar o programa.')
    print ('O maior número é {} e o menor número é {}, já a média de todos os {} valores é de {:.2f}.'.format(m, me, contv+1, media))      