#Este código realiza um cadastro de números e os mostra em ordem crescente.
#Eric Peneres Carneiro#

l = []
e = 'N'

while True:
    n = int (input ('Insira um número para cadastrar na lista: '))
    if n in l:
        print ('Você inseriu um número repetitivo e por isso ele será desconsiderado.')
    else:    
        l.append(n)
    es = str (input ('Quer continuar? [S/N]? ')).upper().strip()
    if es == e:
        break

cr = sorted(l)     
print (f'Todos os números inseridos em ordem crescente são {cr}.')  
