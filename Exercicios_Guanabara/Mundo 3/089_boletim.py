#Este código simula um sistema de boletim escolar com base no exercício 89.
#Eric Peneres Carneiro#

#O sistema funcionará como um boletim escolar.
#Nele incluirá o cadastro e consulta de notas de alunos.
#Ao cadastrar um aluno o programa deverá armazenar cada aluno e suas correspondentes notas.

#============================================================================================#

#Inserir nome e 2 notas do aluno.
#Colocar os respectivos dados em uma lista.
#Montar um menu mostrando as notas dos vários alunos cadastrados, incluindo nome e número.  
#Permitir a consulta através das coordenadas da lista.

listatemporaria = []
boletim = []

print ('=' * 10, 'BOLETIM ESCOLAR', '=' * 10)

while True:
    nome = str (input ('Insira o nome do aluno: ')).capitalize()
    nota1 = float (input ('Insira a primeira nota do aluno: ').strip())
    nota2 = float (input ('Insira a segunda nota do aluno: ').strip())
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resposta = str (input ('Quer continuar? [S / N] ')).upper()
    if resposta in 'N':
        break
  
print ('=' * 10, 'BOLETIM', '=' * 10)

print ('No', 'NOME', '                ', 'MÉDIA')
print ('-' * 30)
for numero, alunos in enumerate(boletim):
    print (f'{numero:<}', end = ' ')
    print (f'{alunos[0]:<26}', end = ' ')
    print (f'{alunos[2]}')

print ('=' * 30)    

while True:
    e = int (input ('Quer ver as notas de qual aluno? (Digite o número na chamada) (Digite 999 para finalizar a consulta)'))
    if e <= len(boletim) - 1:
        print (f'Aluno(a) {boletim[e][0]} tirou as notas {boletim[e][1]}.')
    elif e == 999:
        break    
