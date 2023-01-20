#Este código simula o cadastro de um trabalhador.
#Eric Peneres Carneiro#
 
import datetime
anoatual = datetime.date.today().year

dados = {}

dados["Nome"] = str (input ('Insira o nome do trabalhador: ')).capitalize()
ano = int (input ('Insira o seu ano de nascimento: ').strip())
idade = anoatual - ano
dados["Idade"] = idade
numeroctps = int (input ('Insira aqui o número da carteira de trabalho: '))
if numeroctps != 0:
    dados["No° CTPS"] = numeroctps
    anodecontratacao = int (input ('Insira o seu ano de contratação: ').strip())
    dados ["Ano de Contratação"] = anodecontratacao
    dados ["Salário"] = int (input ('Insira o seu salário: '))
    anoaposentadoria = (anodecontratacao + 35) - ano
    dados ["Aposentadoria"] = anoaposentadoria

for d, v in dados.items():
    print (d, v)
    