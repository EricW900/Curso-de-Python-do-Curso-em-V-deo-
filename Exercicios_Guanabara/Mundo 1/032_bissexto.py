#Este código verifica se um ano inserido pelo usuário é bissexto ou não
#Eric Peneres Carneiro#

a = int (input ('Insira aqui um ano e veremos se ele é bissexto ou não: '))
print (f'O ano {a} é bissexto' if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 else f'O ano {a} não é bissexto')