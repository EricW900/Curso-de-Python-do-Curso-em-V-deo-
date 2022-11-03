#Este código simula um sistema de alistamento militar.
#Eric Peneres Carneiro#

#Ler o ano de nascimento de um jovem.
#Mostrar se ele está apto a se alistar, se ainda vai se alistar ou se já passou da idade do alistamento
#Mostrar também quanto falta ou o tempo que passou do alistamento.

from datetime import date

print ('-=-' * 15)
print ('Sistema de Alistamento Militar')
print ('-=-' * 15)

a = int (input ('Insira o seu ano de nascimento: '))
s = str (input ('Insira o seu sexo (F para Feminino e M para Masculino): ')).upper().strip()
ca = date.today().year
i = a - ca
ab = abs(i)

if s == 'F':
    print ('Você não vai precisar participar do Alistamento Obrigatório.')
else:
    print ('Você irá precisar participar do Alistamento Obrigatório!')    

if ab == 18 and s == 'M':
    print ('-=-' * 15)
    print ('Você tem 18 anos de idade está apto para se alistar!')
    print ('-=-' * 15)
elif ab > 18 and s == 'M':
    ie = ab - 18 
    print ('-=-' * 15)
    print ('Você possui {} anos de idade'.format(ab))
    print ('ATENÇÃO! Você excedeu a idade em {} anos, apresente-se o mais breve o possível na sua Junta Militar!'.format (ie))
    print ('O seu alistamento deveria ter sido em {}'.format (a + 18))
    print ('-=-' * 15) 
else:
    if ab < 18 and s == 'M':
        ia1 = ab - 18
        ia = abs(ia1)
        print ('-=-' * 15)
        print ('Você possui {} anos de idade'.format(ab))
        print ('Você ainda não chegou na idade de alistamento, faltam {} anos para você estar apto para o Alistamento Militar!'.format(ia))
        print ('O seu alistamento será em {}.'.format (a + 18))
        print ('-=-' * 15)