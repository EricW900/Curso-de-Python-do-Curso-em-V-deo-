#Este código mostra o cadastro de um grupo de pessoas.
#Eric Peneres Carneiro#

from statistics import mean

pessoas = []
cadastro = {}
media = []


while True:
    cadastro["Nome"] = str (input ('Insira o nome da pessoa a ser cadastrada: ')).upper()
    idade = int (input ('Insira a idade da pessoa a ser cadastrada: ').strip())
    media.append(idade)
    cadastro["Idade"] = idade
    cadastro["Sexo"] = str (input ('Insira o sexo da pessoa [M/F]: ')).upper() 
    pessoas.append(cadastro.copy())
    r = str (input ('Quer continuar? [S/N] ')).upper()
    if r in 'N':
        break

print (f'O grupo tem o total de {len(pessoas)} pessoas')
print (f'A média de idade do grupo é de {mean(media)}')
for p in pessoas:
    if p["Sexo"] in 'F':
        print (f'Sexo feminino temos: {p["Nome"]}.')

for pe in pessoas:
    if pe["Idade"] > mean(media):
        print (f'{pe["Nome"]}, do sexo {pe["Sexo"]} tem {pe["Idade"]} anos e está acima da média.')        