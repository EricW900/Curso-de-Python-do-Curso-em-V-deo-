#Este código mostra as informações referentes a letra "a" na frase inserida pelo usuário
#Eric Peneres Carneiro#

frase = str (input ('Insira uma frase: ')).strip().lower()
print ('A frase contém {} palavras "A".'.format (frase.count('a')))
print ('A primeira palavra A está localizada na posição {} e a segunda palavra A está localizada na posição {}.'.format (frase.find('a')+1, frase.rfind('a')+1))