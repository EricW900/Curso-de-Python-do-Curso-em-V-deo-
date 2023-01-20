#Este código faz a analise de pessoas que são cadastradas pelo usuário.
#Eric Peneres Carneiro#

listap = []
lista = []

while True:
    listap.append(str(input('Insira um nome: ')))
    listap.append(float(input('Insira um peso: ')))
    lista.append(listap[:])
    listap.clear()
    r = str (input ('Quer continuar? [S / N] ')).upper()
    if r in 'N':
        break

print (f'Ao todo foram cadastradas {len(lista)} pessoas!')
for p in lista:
    if p[1] == 100:
        print (f'O maior peso é de 100Kg e quem pesa ele são {p[0]}')    
    if p[1] == 70: 
        print (f'O menor é de 70Kg e quem pesa ele são {p[0]}.')    
