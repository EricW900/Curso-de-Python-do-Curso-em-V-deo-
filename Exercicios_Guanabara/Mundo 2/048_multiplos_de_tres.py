#Este código calcula todos os números impares que são múltiplos de três.
#Eric Peneres Carneiro#

#Gerar uma lista com números de 1 a 500.
#Verificar quais impares são múltiplos três.
#Calcular os números verificados.

s = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        s += c
print ('A soma de todos os valores impares que são divisíveis por três é {}.'.format(s))       