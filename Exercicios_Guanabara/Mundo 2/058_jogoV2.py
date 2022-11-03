#Este código é um aprimoramento do jogo de adivinhação.
#Eric Peneres Carneiro#

import random

conte = 0
n = 0
print ('-=-' * 20)
print ('JOGO DA ADIVINHAÇÃO!')
print ('-=-' * 20)
nn = int (input ('Insira aqui um número entre 1 e 10 e vejamos se você vai acertar: '))

while nn > 10 or nn < 0:
    print ('-=-' * 20)
    nn = int (input ('Você inseriu o número {}! Insira apenas um número entre 1 a 10: '.format (nn))) 

while nn != n:
    conte += 1
    n = random.randint(1, 10)
    print ('-=-' * 20)
    nn = int (input ('Você errou! O número inserido foi {} e o número gerado foi {}. Tente novamente: '.format(nn, n)))
    while nn > 10 or nn < 0:
        print ('-=-' * 20)
        nn = int (input ('Você inseriu o número {}! Insira apenas um número entre 1 a 10: '.format(nn)))    
if nn == n:
    print ('-=-' * 20)
    print ('Parabéns, você venceu o jogo! O número inserido foi {} e o número gerado foi {}.'.format(nn, n))
    print ('-=-' * 20)
    print ('Você levou ao todo {} tentativas até acertar o número!'.format(conte))