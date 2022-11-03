#Este código mostra o nome completo, o primeiro nome e o último nome de um nome inserido pelo usuário.
#Eric Peneres Carneiro#

n = str (input ('Insira um nome: ')).strip()
nd = n.split()
print ('O nome completo é {}.\nO primeiro nome é {}.\nO último nome é {}.'.format (n, nd[0], nd[-1]))