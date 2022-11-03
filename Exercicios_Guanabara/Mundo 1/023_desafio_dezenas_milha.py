#Este código mostra as informações pertinentes a um número inserido pelo usuário com base no desafio 23
#Eric Peneres Carneiro#

n = str (input ('Insira um número de 0 a 9999: '))
print ('O número de milhar é {}, de centenas é {}, de dezenas é {} e de unidade é {}.'.format (n[0:1], n[1:2], n[2:3], n[3:4]))