#Este código verifica se uma palavra inserida é um palíndromo.
#Eric Peneres Carneiro#

f = str (input ('Insira aqui a frase e veremos se ela é um palíndromo: ')).upper().replace(" ", "")
print ('A palavra inserida é um palíndromo!' if f == f[::-1] else 'A palavra inserida não é um palíndromo.')