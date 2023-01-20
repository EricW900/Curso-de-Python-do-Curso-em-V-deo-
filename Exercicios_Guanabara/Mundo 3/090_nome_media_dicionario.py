#Este código mostra a média de um aluno no dicionário.
#Eric Peneres Carneiro#

aluno = {}
aluno['Nome'] = str (input ('Insira o nome do aluno: ')).capitalize()
aluno['Média'] = float (input (f'Insira a média do(a) {aluno["Nome"]}: '))
if aluno['Média'] > 7.0:
    print (f'A média do(a) {aluno["Nome"]} é {aluno["Média"]} e ele(a) foi aprovado!')
else:
    print (f'A média do(a) {aluno["Nome"]} é {aluno["Média"]} e ele(a) foi reprovado!')    
