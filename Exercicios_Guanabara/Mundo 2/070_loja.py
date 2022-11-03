#Este código simula um sistema de compras de uma loja.
#Eric Peneres Carneiro#


#Ler o nome e preço de vários produtos.
#Perguntar se o usuário quer continuar.
#No final mostrar o total da compra, quantos produtos custam mais de R$1000 e o nome do produto mais barato.


cont = soma = p1000 = pb = maiorp = menorp = 0
pmb = pmc = ''

print ('Bem vindo!')

while True:
    n = str (input ('Insira o nome do produto: '))   
    p = int (input ('Informe o preço do produto: R$')) 
    cont += 1   
    soma += p   
    if cont == 1 or p < menorp:
        menorp = p
        pmb = n   
    if p > 1000:
        p1000 += 1
    e = str (input ('Quer continuar? Se sim S e se não N! ')).upper()
    if e == 'N':
        break  

print (f'O total da sua compra foi de R${soma}, {p1000} produtos custam mais de R$1000 e o nome do produto mais barato é {pmb}.')

              