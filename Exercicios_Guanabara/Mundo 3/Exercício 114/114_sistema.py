from Lib.interface import *
from Lib.bd import *
from time import sleep

bancodedados = 'Banco de Dados.txt'

if not verificarBD(bancodedados):
    criarBD(bancodedados)

while True:
    menu(['Ver pessoas cadastradas', 'Cadastrar Nova pessoa', 'Sair do Sistema'])
    opcao = leiaescolha('Digite sua opção: '.strip())
    sleep(0.4)
    if opcao == 1:
        sleep(0.4)
        lerBD(bancodedados)        
    elif opcao == 2:
        sleep(0.4)
        nome = str(input ('Insira o nome da pessoa: ')).upper()
        idade = leiaescolha('Insira a idade da pessoa'.strip())
        cadastroBD(bancodedados, nome, idade)
    elif opcao == 3:
        print ('Finalizando...')
        sleep(0.4)        
        break
    else:
        cabecalho('ERRO! Digite uma opção válida'.center(30))
