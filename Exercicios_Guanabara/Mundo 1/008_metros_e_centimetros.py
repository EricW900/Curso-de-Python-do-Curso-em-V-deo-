#Este código converte metros em centímetros e em milímetros
#Eric Peneres Carneiro


m = float (input ('Insira aqui a quantidade em metros para ser convertida em centimetros e milímetors: '))
print ('A conversão de {} metros para centímetros é {}cm.\nE para milímetros é {}mm.\nE para Kilometros é {}Km.\nE para Hectometro é {:.2f}Hm. \nE para Decâmetro é {:.1f}Dam.'.format(m, m*100, m*1000, m/1000, m*0.01, m*0.10))