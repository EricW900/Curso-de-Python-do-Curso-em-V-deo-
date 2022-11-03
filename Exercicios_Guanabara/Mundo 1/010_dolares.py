#Este código converte real em dólar com base na cotação do dia 28/10/2022.
#1 real equivale a 0.19 dólares americanos
#Eric Peneres Carneiro

r = float (input ('Quantos reais você tem na sua carteira? R$'))
print ('Você pode converter R${} em até US${:.2f}'.format (r, r*0.19))