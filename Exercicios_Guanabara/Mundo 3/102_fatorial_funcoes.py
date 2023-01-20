#Este código calcula o resultado de uma fatorial com resposta personalizada utilizando funções
#Eric Peneres Carneiro#

def fatorial(num, flag=False):
    """
    Esta função calcula um fatorial de um número informado pelo usuário.
    num = Número informado
    flag = False, caso queira apenas o resultado. Se quiser mostrar a conta, colocar como True.
    """
    if flag == False:
        for numeros in range(num-1, 0, -1):
            num *= numeros
        return num
    else:
        for numeros in range(num-1, 0, -1):
            num *= numeros
            print(f'{numeros} x ', end='')
        print (f' = ', end='')
        return num

num = int (input ('Insira um número para calcularmos sua fatorial: '))
    
print(fatorial(num, False))


