#Este código é a junção de todos os exercícios das aulas de modularização de Python do Curso em Video
#Eric Peneres Carneiro#

from utilidadesCeV import moedas, dados
#106 - 107

preco = float (input ('Insira aqui o preço em R$'))
aumento = int (input ('Insira quantos por cento você quer aumentar: '))
diminuir = int (input ('Insira quantos por cento você quer diminuir: '))


print(f'A metade de {moedas.conversao(preco)} é {moedas.conversao(moedas.metade(preco))}.')
print(f'O dobro de {moedas.conversao(preco)} é {moedas.conversao(moedas.dobro(preco))}.')
print(f'O aumento de {aumento}% é de {moedas.conversao(moedas.aumentar(preco, aumento))}.')
print(f'A diminuição de {diminuir}% é de {moedas.conversao(moedas.diminuir(preco, diminuir))}.')

#108 
 
preco = float (input ('Insira aqui o preço em R$'))
aumento = int (input ('Insira quantos por cento você quer aumentar: '))
diminuir = int (input ('Insira quantos por cento você quer diminuir: '))

print(f'A metade de R${preco} é {moedas.metade(preco, True)}')
print(f'O dobro de R${preco} é {moedas.dobro(preco, True)}')
print(f'O aumento de {aumento}% é {moedas.aumentar(preco, aumento, True)}')
print(f'A diminuição de {diminuir}% é {moedas.diminuir(preco, diminuir, True)}')

#109-110

preço = float (input ('Insira o preço: '))
a = int (input ('Insira o aumento: ').strip())
r = int (input ('Insira a redução: ').strip())
moedas.resumo(preço, a, r)

#111 - 112

preço = dados.leiaint('Digite um preço R$')
a = int (input ('Insira o aumento: ').strip())
r = int (input ('Insira a redução: ').strip())
moedas.resumo(preço, a, r)
