#Este código é um painel de operações para dois números inseridos pelo usuário.
#Eric Peneres Carneiro#

f = 5

n1 = int (input ('Insira aqui um número: '))
n2 = int (input ('Insira aqui outro número: '))

print ('Os números inseridos foram {} e {}.'.format (n1, n2))

while f == 5:
    print ('-=-' * 20)
    e = int (input ('Que tipo de operação você deseja fazer?\n[ 1 ] soma \n[ 2 ] multiplicação \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n'))
    while e != 1 and e != 2 and e != 3 and e != 4 and e != 5:
        e = int (input('Opção inválida, tente novamente \n[ 1 ] soma \n[ 2 ] multiplicação \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \n ')) 
    if e == 1:
        print ('-=-' * 20)
        print ('Você escolheu somar os valores.')
        print ('A soma de {} + {} = {}.'.format(n1, n2, n1 + n2 ))
    if e == 2:
        print ('-=-' * 20)
        print ('Você escolheu multiplicar os dois números.')
        print ('A múltiplicação de {} * {} = {}.'.format(n1, n2, n1 * n2))
    if e == 3:
        print ('-=-' * 20)
        print ('Você escolheu verificar quais números são maiores que os outros.')
        ma = me = n2
        if n1 > n2:
            ma = n1
        if n1 < n2:
            me = n1
        print ('O maior número é {} e o menor número é {}.'.format(ma,me))
    if e == 4:
        print ('Você escolheu digitar novos números: ')
        n1 = int (input ('Insira aqui um novo número: '))
        n2 = int (input ('Insira aqui outro novo número: '))
        print ('Agora os novos números são {} e {}!'.format (n1, n2))    
    if e == 5:
        print ('Obrigado por utilizar o painel, tenha um bom dia!')
        break    