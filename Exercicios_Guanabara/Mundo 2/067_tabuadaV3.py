#Este código mostra uma tabuada que será criada com base no número digitado pelo usuário.
#Eric Peneres Carneiro#

n = 0
while True:
    n = int (input ('Quer ver a tabuada de qual valor? '))
    if n <= 0:
        break
    for i in range (1, 11):
        print (f' {n} x {i} = {n * i}')
print ('Fim da tabuada')        