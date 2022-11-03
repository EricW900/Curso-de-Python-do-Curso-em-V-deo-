#Este código pede um número inteiro ao usuário e converte o número em uma opção selecionada.
#Eric Peneres Carneiro# 

#Pedir um número inteiro
#Pedir para o usuário escolher um base de conversão (B = Binário, O = Octal e H = Hexadecimal)
#Mostrar na tela o número convertido
 
v = int (input ('Insira aqui um número inteiro: '))
b = str (input ('Insira aqui a base para conversão (B para Binário, O para Octal e H para Hexadecimal.): ')).upper()

if b == 'B':
    vc = bin(v)
    print ('Você selecionou a conversão para Binário e o valor {} foi convertido para {}.'.format(v, vc [2:]))
elif b == 'O':
    vc = oct(v)
    print ('Você selecionou a conversão para Octal e o valor {} foi convertido para {}.'.format(v, vc [2:]))
elif b == 'H':
    vc = hex(v)
    print ('Você selecionou a conversão para Hexadecimal e o valor {} foi convertido para {}.'.format(v, vc [2:]))