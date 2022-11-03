#Este código mostra se o nome de uma cidade inserida pelo usuário começa "Santo", com base no exercício 24.
#Eric Peneres Carneiro#

c = str (input ('Coloque aqui o nome de uma cidade: ')).strip().capitalize()
c = c.split()
print ('Caso a cidade tenha "Santo" no início nome, o programa ira mostrar True, caso contrário, mostrará False.\n{}'.format ('Santo' in c[0]))