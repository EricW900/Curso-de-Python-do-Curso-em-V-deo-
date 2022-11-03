#Este código sorteia a a ordem de apresentação de trabalhos
#Eric Peneres Carneiro#  

import random

a1 = 'Miller'
a2 = 'Ryan'
a3 = 'Daniel Jackson'
a4 = 'Michael'
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print ('A ordem de apresentação dos trabalhos foi sorteada e ficou da seguinte maneira: \n{}'.format (alunos))