#Este código pede para o usuário inserir um número de 0 a 998 e após finalizar a contagem, ele mosttra a soma e a quantidade de números inseridos.
#Eric Peneres Carneiro# 

n = s = cont = 0

while True:
    n = int (input ('Insira aqui um número válido de 0 a 998 (999 para interromper.): '))
    if n == 999:
        break
    cont += 1
    s += n
print (f'A soma dos {cont} números é de {s}.')    