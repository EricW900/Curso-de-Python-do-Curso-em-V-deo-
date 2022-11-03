#Este código é um jogo de par ou impar.
#Eric Peneres CarneirO# 

from random import randint

#Iniciando as variáveis

p = i = ' '
npc = randint(0, 10)
n = s = 0
contv = 0

while True:
    print (f'-=-' * 20)
    print ('PAR OU IMPAR!')
    print (f'-=-' * 20)
    n = int (input ('Insira um número: ')) #Inserir número.

    if n > 10: #Verificação do número.
        n = int (input ('Insira um valor válido de 1 a 10: '))
    p = str (input ('Par ou Impar? [P / I] ')).upper().strip() #Selecionar par ou impar.
    s = n + npc

    if p == 'P': #Se a condição escolhida foi Par.
        if s % 2 == 0: #Checando se é um número Par
            print (f'-=-' * 20)
            print ('Você ganhou!')
            print ('Você selecionou Par!')
            print (f'Você jogou {n} e o computador jogou {npc}! Ambos os números somados são {s} e ele é dá Par!')            
            npc = randint(0,11)
            s = n + npc
            contv += 1             
        else:
            if s % 2 != 0:
                print (f'-=-' * 20)
                print ('Você selecionou Par!')
                print ('Você perdeu!')
                print (f'Você jogou {n} e o computador jogou {npc}! Ambos os números somados são {s} e ele é dá Impar!')
                break

    if p == 'I': #Se a condição escolhida foi Impar.
        if s % 2 != 0: #Checando se é um número Impar.
            print (f'-=-' * 20)
            print ('Você selecionou Impar!')
            print ('Você ganhou!')
            print (f'Você jogou {n} e o computador jogou {npc}! Ambos os números somados são {s} e ele é Impar!')
            npc = randint(0, 10)
            s = n + npc
            contv += 1
        else:
            if s % 2 == 0:
                print (f'-=-' * 20)
                print ('Você selecionou Impar!')
                print ('Você perdeu!')
                print (f'Você jogou {n} e o computador jogou {npc}! Ambos os números somados dão {s} e ele é Par ')
                break
print (f'-=-' * 20)            
if contv != 0: #Contador de vitórias.
    print (f'Você venceu {contv} vezes!')            
print ('Fim! Obrigado por jogar.')            