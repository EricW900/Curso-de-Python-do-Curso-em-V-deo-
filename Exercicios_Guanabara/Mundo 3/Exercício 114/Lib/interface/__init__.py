def leiaescolha (opcao):
    while True:
        try:
            p = int(input(opcao))
            '''if p == 3:
                break'''
        except ValueError:           
            print ('Tem algo de errado com sua escolha! Tente novamente: ')
        except KeyboardInterrupt:
            print ('Você decidiu finalizar o programa!')
            break
        else:
            return p


def linha():
    print ('=' * 30)


def cabecalho(msg):
    linha()
    print(msg.center(30))
    linha()


def menu(lista):
    cabecalho('Menu Principal'.center(30))
    c = 1
    for opcao in lista:
        print (f'{c} - {opcao}')
        c += 1

