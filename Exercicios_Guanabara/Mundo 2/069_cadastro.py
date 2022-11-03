#Este código é um sistema de cadastro de pessoas.
#Eric Peneres Carneiro#


#Ler a idade e sexo de várias pessoas
#A cada pessoa cadastrada, verificar se quer continuar o cadastro
#Ao final mostrar quantas pessoas tem mais de 18, quantos homens foram cadastrados e quantas mulheres tem 
#menos de 20.
  

conti = conth = contm20 = 0


print ('Bem vindo ao cadastro!')
while True:
    s = str (input ('Insira o sexo da pessoa a ser cadastrada [M / F]:  ')).upper().strip()
    i = int (input ('Insira a idade da pessoa a ser cadastrada: '))
    while s not in 'MF':
        print ('Dado inválido')
        s = str (input ('Insira o sexo da pessoa a ser cadastrada [M / F]:  ')).upper().strip()          
    if s == 'M':        
        conth += 1    
        if i > 18:
            conti += 1
            print ('Pessoa cadastrada!')
        if i < 18:
            print ('Pessoa cadastrada!')
        e = str (input ('Quer continuar? [S / N] ')).upper().strip()
        while e not in 'NS':
            print ('Opção inválida!')
            e = str (input ('Quer continuar? [S / N] ')).upper().strip()
        if e == 'N':
            break 

    if s == 'F':        
        if i < 20:
            contm20 += 1            
        if i > 18:
            conti += 1
        e = str (input ('Quer continuar? [S / N] ')).upper().strip()
        while e not in 'NS':
            print ('Opção inválida!')
            e = str (input ('Quer continuar? [S / N] ')).upper().strip()
        if e == 'N':
            break                                        

print (f'Ao todo {conti} pessoas tem mais de 18 anos, {conth} homens foram cadastrados e {contm20} mulheres possuem menos de 20 anos.')        