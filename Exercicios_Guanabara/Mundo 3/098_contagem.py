#Este código cria um contador com utilizando funções
#Eric Peneres Carneiro#

from time import sleep

def linha():
    print ('-=' * 30)


def contagem(con):
    for n in range(1, con + 1):
        sleep(0.2)
        print (n, end= ' ', flush=True)
    print ('Fim!')


def contagem1(con):
    for n in reversed(range(0 , 10 + 1, 2)):
        sleep(0.2)
        print(n, end= ' ', flush=True)        
    print ('Fim!')

def contagem2(i, f, p):
    if p == 0:
        p = 1

    if i < f:
        for n in range(i, f + 1, p):
            sleep(0.2)
            print(n, end= ' ', flush=True)
        print('Fim!')
    elif i > f or p < 0:
        if i > f and p > 0:
            for n in reversed(range(f, i + 1, p)):
                sleep(0.2)
                print(n, end= ' ', flush=True)
            print('Fim!')
        else:
            if p < 0:
                p *= -1
                for n in reversed(range(f, i + 1, p)):
                    sleep(0.2)
                    print(n, end= ' ', flush=True)
                print('Fim!')                   


con = 10
linha()
contagem(con)
linha()
contagem1(con)
linha()
i = int (input ('Insira o inicío: '))
f = int (input ('Insira o final: '))
p = int (input ('Insira o passo: ')) 
linha()
contagem2(i, f, p)
 
print ('Fim do programa!')
