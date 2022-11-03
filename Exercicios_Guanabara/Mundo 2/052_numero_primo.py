#Este código mostra se um número é primo ou não.
#Eric Peneres Carneiro#

contador = 0
n = int (input ('Insira aqui um número: '))

for i in range(1, n+1):    
    if n % i == 0:
        contador += 1
print ('O número {} é divisivel em {} vezes.'.format (n, contador))
if contador == 2:
    print ('Isso faz dele um número primo')
else:
    print ('Isso não faz dele um número primo')