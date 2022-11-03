#Este código calcula o dobro, o triplo e a raiz quadrada de um número inserido
#Eric Peneres Carneiro

n = int (input ('Insira aqui o número para vermos o seu dobro, o triplo e a sua raiz quadrada: '))
print ('O dobro do número inserido é {}.\nO triplo é {}.\nE a raiz quadrada é {:.2f}.'.format(n*2, n*3, n**(1/2)))