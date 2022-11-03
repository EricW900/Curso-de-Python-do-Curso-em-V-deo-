#Este código mostra se um nome contém "Silva" com base no exercício 25.
#Eric Peneres Carneiro# 

n = str (input ('Insira aqui o nome: ')).strip().title()
print ('Caso o nome contenha "Silva", o programa irá mostrar True, caso o contrário, o programa irá mostrar "False". \n{}'.format ('Silva' in n))