#Este código calcula a média de uma turma utilizando uma função
#Eric Peneres Carneiro#


def boletim (*n, detalhe = False):
    """
    Esta função calcula a média de notas de uma turma!
    n vai receber as notas.
    detalhe = False, caso não queira ver a situação da turma, caso queira, digite True
    """
    dados = {}
    dados['Maior'] = max(n)
    dados['Menor'] = min(n)
    dados['Quantidade'] = len(n)
    dados['Média'] = sum(n) / dados["Quantidade"]
    if detalhe := True:
        if dados['Média'] >= 7.0:
            print('Turma aprovada!')
        elif dados['Média'] >= 5.0 and dados['Média'] < 7.0:
            print ('Turma de recuperação!')
        else:
            if dados['Média'] < 5.0:
                print('Turma reprovada!')
    print (dados)

boletim(9.5, 8.6, 8.2, 7.9, True)
