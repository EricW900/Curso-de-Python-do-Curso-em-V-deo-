#Este código acessa o menu do Python de uma maneira exigida no exercicio 106.
#Por algum motivo as cores, que eram um pré-requisito para o exercício, não estavam funcionando, portanto decidi deixar ele sem cores.
#Eric Peneres Carneiro#

def menu(msg):
    print ('=' * 35)
    print(f'  Acessando a biblioteca de {msg}.')
    print ('=' * 35)
    cmd2 = msg
    help(cmd2)


while True:
    cmd = str (input ('Insira aqui o que você quer ver da biblioteca Python: ')).lower()
    if cmd == 'fim':
        print ('FIm do programa!')
        break
    menu(cmd)
