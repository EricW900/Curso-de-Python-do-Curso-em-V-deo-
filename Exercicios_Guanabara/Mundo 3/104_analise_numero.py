#Este código verifica se um número é inteiro ou não
#Eric Peneres Carneiro#


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print (f'Digite um número válido!')
        if ok:
            break
    return valor

n = leiaint("Digite um número: ")
print(f'Você digitou o número {n}')
