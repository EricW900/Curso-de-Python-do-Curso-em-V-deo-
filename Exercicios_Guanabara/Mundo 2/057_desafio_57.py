#Este código verifica se um sexo é masculino ou feminino, caso não seja, ele pede ao usuário para inserir novamente.
#Eric Peneres Carneiro# 

s = str (input ('Insira aqui o seu sexo: ')).upper().strip()

while s not in 'MF'  :
    s = str (input ('Sexo invalido, digite novamente: ')).upper().strip()
if s == 'F':
    print ('Você escolheu o sexo Feminino.')
else:
    print ('Você escolheu o sexo Masculino.')    