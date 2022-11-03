#Este código simula a contagem regressiva para o lançamento de fogos de artíficio.
#Eric Peneres Carneiro#

from time import sleep


print ('Vamos estourar uns fogos de artíficio?')
for f in range (10, -1, -1):
    sleep(1)
    print (f, '<--')
print ('Kabuuuuuumm!!')