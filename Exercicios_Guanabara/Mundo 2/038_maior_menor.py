#Este código compara dois valores e mostra qual é o maior ou menor.
#Eric Peneres Carneiro#

v = int (input ('Insira aqui um valor: '))
v2 = int (input ('Insira aqui outro valor: '))

if v > v2:
    print ('O primeiro valor é maior.')
elif v2 > v:
    print ('O segundo valor é maior.')
else:
    if v == v2:
        print ('Ambos os valores são iguais')