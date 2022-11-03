#Este código calcula todos os números inseridos em uma lista.
#Eric Peneres Carneiro#

l = []
cont = 0
n = int (input ('Insira aqui um número entre 1 e 999: '))

while n < 999:
    cont += 1
    l.append(n)
    n = int (input ('Adicione mais números: '))
print ('A soma de todos os {} valores inseridos é de {}.'.format(cont , sum(l)))