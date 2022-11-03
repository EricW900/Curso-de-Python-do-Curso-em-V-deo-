#Este código calcula a média de um aluno
#Eric Peneres Carneiro#

n1 = float (input ('Insira aqui a primera nota do aluno: '))
n2 = float (input ('Insira aqui a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media >= 7:
    print (f'A média do aluno foi {media}')
    print ('Aprovado!')
elif media >= 5 and media <= 6.9:
    print (f'A média do aluno foi {media}')
    print ('Recuperação!')
elif media < 5:
    print (f'A média do aluno foi {media}')
    print ('Reprovado!')