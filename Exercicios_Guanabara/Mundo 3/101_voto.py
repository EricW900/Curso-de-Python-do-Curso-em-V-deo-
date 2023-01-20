#Este código calcula se uma pessoa está apta a votar ou não utilizando funções.
#Eric Peneres Carneiro#

import datetime


def calculovoto(anonascimento):    
    idade = datetime.date.today().year - anonascimento
    if idade >= 16 and idade < 18:
        print (f'Com {idade} anos o seu voto é opcional.')
    elif idade > 18 and idade < 65:
        print (f'Com {idade} anos o seu voto é obrigatório!')  
    elif idade < 16:
        print (f'Com {idade} anos o seu voto foi negado!')
    else:
        print (f'Com {idade} anos o seu voto é opcional.')    

print (f'Vamos ver se você está apto a votar?')
anonascimento = int (input ('Insira o seu ano de nascimento: ').strip())       

calculovoto(anonascimento)        
