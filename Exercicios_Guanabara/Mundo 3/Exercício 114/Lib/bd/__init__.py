from Lib.interface import *


def verificarBD (nome):
    try:
        nome = open(nome, 'rt')
        nome.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarBD (nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close
    except:
        print (f'Houve um erro na criação do Banco de Dados.')
    else:
        print (f'Banco de Dados com nome "{nome}" criado com sucesso!')


def lerBD (nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print ('Erro ao ler o arquivo!')
    else:
        cabecalho('Lista de pessoas')
        for linha in arquivo:
            dado = linha.split(' ')
            dado[0] = dado[0].replace('\n', '')
            print(f'{dado[0]} anos')
    finally:
        arquivo.close()


def cadastroBD (bd, nome = 'Não existe', idade = '0'):
    try:
        bd = open(bd, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            bd.write(f'{nome}\t{idade}\n')
        except:
            print (f'Houve um ERRO na hora de escrever os dados!')
        else:
            print (f'Novo cadastro de {nome} adicionado ao banco de dados!')
            bd.close()