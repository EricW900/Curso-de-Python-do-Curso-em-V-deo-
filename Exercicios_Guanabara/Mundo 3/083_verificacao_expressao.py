#este código é um verificador de expressões matemáticas.
#Eric Peneres Carneiro#

l = []

e = str (input ('Insira uma expressão matemática: '))
for s in e:
    if s == '(':
        l.append('(')
    elif s == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print ('É válida!')
else:
    print ('Não é válida!')  
                      