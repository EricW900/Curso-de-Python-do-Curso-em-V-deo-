#Este código pede que o usuário insira algo e ele irá mostrar todas as informações referentes ao que foi inserido
#Eric Peneres Carneiro#

algo = input ('Digite algo e todas as informações referentes a ele serão mostradas: ')

#Classe Primitiva

print ('É uma classe primitiva', type(algo))

#É númerico?

if algo.isnumeric() == True:
    print ('É um número')
else:
    print ('Não é um número')

#É maiúsculo?        

if algo.isupper() == True:
    print ('Está em maiúsculo')
else:
    print ('Não está em maiúsculo')

#Contém espaço?    

if algo.isspace() == True:
    print ('Não contém espaço')
else:
    print ('Contém espaço')

#Tem no alfabeto?  

if algo.isalpha() == True:
    print ('Tem no alfabeto')
else:
    if algo.isalpha() == False:
        print ('Não tem no alfabeto')

#É alfanumérico?

if algo.isalnum() == True:
    print ('É alfanumérico')
else:
    print ('Não é alfanumérico')

#Está em minúsculo?    

if algo.islower() == True:
    print ('Está em minúsculo') 
else:
    print ('Não está em minúsculo')

#Está capitalizada?

if algo.istitle() == True:
    print ('Está capitalizada')
else:
    print ('Não está capitalizada')                   