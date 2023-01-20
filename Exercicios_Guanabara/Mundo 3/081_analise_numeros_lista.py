#Este código cria uma lista com números inseridos pelo usuário e faz uma analise deles.
#Eric Peneres Carneiro#

l = []
e = 'S'
cont = 0

n = int (input ('Insira um número para compor a lista: '))
l.append(n)
es = str (input ('Quer continuar? [S/N] ')).upper().strip()
while es == e:
    n = int (input ('Insira um número para compor a lista: '))
    l.append(n)
    es = str (input ('Quer continuar? [S/N] ')).upper().strip()
    if es != e:
        print ('Inserção de números finalizada!')
        
ld = l [::]        
   
print ('-=-' * 20)
print (f'A lista digitada foi {sorted(ld, reverse=True)}')   
print (f'Ao todo foram digitados {len(l)} números!')
if 5 in ld:
    print (f'O valor 5 foi digitado e a primeira posição que ele aperece é a posição {ld.index(5)}')
else:
    print ('O valor 5 não foi digitado!')    
print ('-=-' * 20)
