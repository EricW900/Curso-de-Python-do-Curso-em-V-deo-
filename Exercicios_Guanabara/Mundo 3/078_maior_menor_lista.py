#Este código mostra qual o maior e o menor valor de cinco números inseridos pelo usuário.
#Eric Peneres Carneiro#

l = []

for c in range (5):
    n = int (input ('Insira um valor: '))
    l.append(n)
    
m = max(l)
me = min(l)    

print (f'Os valores digitados foram {l}')
print (f'O maior valor da lista é {max(l)} e ele está localizado na posição {l.index(m)}.')
print (f'O menor valor da lista é {min(l)} e ele está localizado na posição {l.index(me)}')