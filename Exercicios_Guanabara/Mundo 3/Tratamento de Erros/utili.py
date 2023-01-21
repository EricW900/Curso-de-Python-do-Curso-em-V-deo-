
def leiaint(n = 0):
    while True:
        try:
            n = int(input(n))
        except TypeError:
            print ('Temos algum erro relacionado ao valor inserido! Certifique-se de digitar um número inteiro!')
            continue
        except ValueError:
            print ('O usuário preferiu não digitar este número!')
            return 0
        except (KeyboardInterrupt):
            print ('Você finalizou o programa.')
        else:
            return n
        
def leiafloat(n = 0):
    while True:
        try:
            n = float(input(n))
        except TypeError:
            print('Temos um erro relacionado ao valor digitado! Certifique-se de digitar um número real!')
            continue
        except ValueError:
            print ('O usuário preferiu não digitar este número!')
            return 0
        except(KeyboardInterrupt):
            print('Você finalizou o programa!')
        else:
            return n

def checasite(url):
    import urllib
    import urllib.request
    try:
        urllib.request.urlopen(url)
    except:
        print ('Não é possível se conectar, talvez você esteja sem internet ou o site está fora do ar.')
    else:
        print ('É possível se conectar ao site.')

    