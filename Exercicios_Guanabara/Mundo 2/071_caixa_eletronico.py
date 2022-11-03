#Este código simula um caixa eletrônico.
#Eric Peneres Carneiro#

v = int (input ('Insira aqui um valor a ser sacado: '))
c = 50
m = v
t = 0
while True:
    if m >= c:
       m -= c
       t += 1         
    else:
        if t > 0:
            print (f'Você irá receber {t} notas de R${c}') 
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        t = 0     
        if m == 0:
            break             