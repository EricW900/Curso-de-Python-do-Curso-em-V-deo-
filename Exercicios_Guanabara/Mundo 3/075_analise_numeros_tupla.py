#Este código realiza a análise de números em uma tupla.
#Eric Peneres Carneiro# 

n1 = int (input ('Insira um número: '))
n2 = int (input ('Insira um número: '))
n3 = int (input ('Insira um número: '))
n4 = int (input ('Insira um número: '))
n5 = int (input ('Insira um número: '))
 
contp = 0

if n1 % 2 == 0:
    contp += 1
elif n2 % 2 == 0:
    contp += 1
elif n3 % 2 == 0:
    contp += 1 
elif n4 % 2 == 0:
    contp += 1
else:
    if n5 % 2 == 0:
        contp += 1                  

l = (n1, n2, n3, n4, n5)

if 3 in l:
    print (f'O primeiro valor 3 foi digitado na posição {l.index(3)}')

print (f'Você digitou os vlores {l}')
print (f'O valor 9 apareceu {l.count(9)} vezes.')
print (f'Ao todo tivemos {contp} números pares.')