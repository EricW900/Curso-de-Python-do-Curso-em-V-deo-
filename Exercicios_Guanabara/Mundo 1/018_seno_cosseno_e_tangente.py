#Este código mostra o seno, cosseno e a tangente de um número inserido pelo usuário
#Eric Peneres Carneiro#

from math import cos, sin, tan, radians

n = int (input ('Insira aqui um angulo e iremos mostrar seu seno, cosseno e tangente: '))
print ('O angulo inserido foi {}°\nE o seu seno é {:.2f}\nO seu coseno é {:.2f}\nE a sua tangente é {:.2f}'.format(n, sin(radians(n)), cos(radians(n)), tan(radians(n))))