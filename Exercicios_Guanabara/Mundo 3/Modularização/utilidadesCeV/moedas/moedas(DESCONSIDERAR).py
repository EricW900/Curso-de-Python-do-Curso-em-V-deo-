

def metade(n, e = False, m = 'R$'):
    resultado = n / 2
    if e == True:
        return f'{m}{resultado}'.replace('.',',')
    else:
        return resultado


def dobro (n, e = False, m = 'R$'):
    dobro = n * 2
    if e == True:
        return f'{m}{dobro}'.replace('.',',')
    else:
        return dobro


def aumentar(n, a, e = False, m = 'R$'):
    aumento = n + (n * a / 100)
    if e == True:
        return f'{m}{aumento}'.replace('.',',')
    else:
        return aumento


def diminuir(n, d, e = False, m = 'R$'):
    diminuir = n - (n * d / 100)
    if e == True:
        return f'{m}{diminuir}'.replace('.',',')
    else:
        return diminuir

def conversao(n = 0, m = 'R$'):
    return f'{m}{n}'.replace('.',',')


def resumo(p, a = 0, r = 0, m = 'R$'):
    print ('=' * 20)
    print ('   RESUMO DO VALOR')
    print ('=' * 20)
    print (f'Preço analisado: \t{m}{p:>2.2f}')
    print (f'Dobro do preço: \t{m}{dobro(p):>2.2f}')
    print (f'Metade do preço: \t{m}{metade(p):>2.2f}')
    print (f'{a}% de aumento: \t\t{m}{aumentar(p, a):>2.2f}')
    print (f'{r}% de redução: \t\t{m}{diminuir(p, r):>2.2f}')


