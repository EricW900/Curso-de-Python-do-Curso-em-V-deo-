

def leiaint(msg):    
    validador = False
    while not validador:
        numero = str(input(msg)).replace(',','.').strip()
        if numero.isalpha() or numero == '':
            print ('Digite um preço válido')
        else:
            validador = True
            return float (numero)
