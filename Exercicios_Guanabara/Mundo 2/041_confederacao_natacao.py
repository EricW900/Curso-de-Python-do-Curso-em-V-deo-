#Este código calcula a idade de um competidor de natação e enquadra ele em uma categoria.
#Eric Peneres Carneiro#

import datetime

a = int (input ('Insira o ano de nascimento do competidor: '))
ano = datetime.date.today().year
i = ano - a

if i <= 9:
    print ('O competidor possui {} anos de idade e se ennquadra na categoria Mirim.'.format(i))
elif i > 9 and i <= 14:
    print ('O competidor possui {} anos de idade e se enquadra na categoria infantil.'.format(i))
elif i > 14 and i <= 19:
    print ('O competidor possui {} anos de idade e se enquadra na categoria Júnior.'.format(i))
elif i > 19 and i <=25:
    print ('O competidor possui {} anos de idade e se enquadra na categoria Sênior.'.format(i))
else:
    if i > 25:
        print ('O competidor possui {} anos de idade e se enquadra na categoria Master.'.format(i))