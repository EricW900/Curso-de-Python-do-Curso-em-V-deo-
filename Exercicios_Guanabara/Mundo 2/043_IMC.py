#Este código calcula o IMC.
#Eric Peneres Carneiro#

#imc = peso / altura²

p = float (input ('Insira aqui o seu peso: Kg'))
a = float (input ('Insira aqui sua altura em metros: '))
imc = p / pow(a, 2)

if imc < 18.5:
    print ('Seu IMC é de {:.1f} e está abaixo do ideal.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print ('Seu IMC é de {:.1f} e está no valor ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print ('O seu IMC é de {:.1f} e está no valor acima do recomendado (Sobrepeso).'.format(imc))
elif imc >= 30 and imc < 40:
    print ('O seu IMC é de {:.1f} e está no valor muito acima do recomendado (Obesidade).'.format(imc))
else:
    if imc > 40:
        print ('O seu IMC é de {:.1f} e está ligeiramente acima do recomendado (Obesidade Mórbida).'.format(imc))    