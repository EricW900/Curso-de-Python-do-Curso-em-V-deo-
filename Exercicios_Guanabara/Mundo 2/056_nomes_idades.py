#Este código realiza a analise de nomes e idades de um grupo de 4 pessoas.
#Eric Peneres Carneiro# 

from numpy import average

li = []

contfem20 = 0
mih = 0
nv = '' 

for f in range (1, 4+1):
    print ('-=-' * 15)
    print ('{}° pessoa.'.format(f))
    s = str (input ('Insira o seu sexo (F para Feminino e M para Masculino): ')).strip().upper()
    if s == 'F':
        print ('-=-' * 15)
        n = str (input ('Insira o seu nome: '))        
        i = int (input ('Insira aqui a sua idade: '))        
        if i < 20:
            li.append(i)            
            contfem20 += 1
        elif i >= 20:
            li.append(i)
    if s == 'M':
        print ('-=-' * 15)
        n = str (input ('Insira o seu nome: '))
        i = int (input ('Insira a sua idade: '))
        if i > mih:
            mih = i
            nv = n

print ('-=-' * 15)
print ('A média das idades é de {:.2f} anos.'.format(average(li)))
print ('Existem {} mulheres com idades abaixo de 20 anos.'.format(contfem20))
print ('O homem mais velho se chama {}.'.format(nv))