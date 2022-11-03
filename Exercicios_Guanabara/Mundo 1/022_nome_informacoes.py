#Este código analisa as informações de um nome inserido pelo usuário
#Eric Peneres Carneiro#

n = str (input ('Insira o seu nome completo aqui: ')).strip()
print ('O nome completo em maiúsculo é: {}\nO nome completo me minúsculo é: {}'.format (n.upper(), n.lower()))
print ('O seu nome possui {} letras e possui {} letras no primeiro nome.'.format(len(n) - n.count(' '), n.find(' ')))