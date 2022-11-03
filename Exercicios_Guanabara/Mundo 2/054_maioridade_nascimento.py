#Este código mostra quantas pessoas atingiram a maioridade e quantas não atingiram a maioridade.
#Eric Peneres Carneiro#

from datetime import date

aa = date.today().year

s = 0
s1 = 0
for i in range (1, 7+1):
    an = int (input ('Insira aqui o ano de nascimento da pessoa: '))
    id = an - aa
    iab = abs(id)
    if iab >= 21:
        s += 1
    elif iab < 21:
        s1 += 1
print ('Ao todo {} pessoas atingiram a maioridade.'.format (s))
print ('Ao todo {} pessoas ainda não atingiram a maioridade.'.format(s1))       