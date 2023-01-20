#Este código mostra um número por extenso que foi inserido pelo usuário entre zero a vinte.
#Eric Peneres Carneiro#

e = 'S'

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = int (input ('Insira um número para vê-lo por extenso: '))
while n > 20 or n < 0:
    n = int (input ('Insira um valor válido entre 0 a 20: '))
print (f'Você digitou {numeros[n]}')

es = str (input ('Quer digitar outro número? [S / N]: ')).upper().strip()
while es == e:
    n = int (input ('Insira outro número: '))
    while n < 0 or n > 20:
        n = int (input ('Insira um valor válido entre 0 a 20: '))
    print (f'Você inseriu o número {numeros[n]}.')
    es = str (input ('Quer digitar outro número? [S / N]: ')).upper().strip()
    if es ==  'N':
        break 