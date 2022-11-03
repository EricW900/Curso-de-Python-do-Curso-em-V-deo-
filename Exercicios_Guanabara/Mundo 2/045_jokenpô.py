#Jokenpô.
#Eric Peneres Carneiro#

from random import choice

jogadas = ['Pedra', 'Papel', 'Tesoura']
mpc = (choice(jogadas))

print ('Vamos jogar Pedra, Papel, Tesoura!')
mj = str (input ('Insira aqui a sua jogada (P = Pedra, A = Papel e T = Tesoura): ')).upper()

if mj == 'T':
    m = 'Tesoura'
elif mj == 'A':
    m = 'Papel'
else:
    if mj == 'P':
        m = 'Pedra'

if m == 'Pedra' and mpc == 'Pedra':
    print ('Você jogou Pedra e o computador jogou Pedra, vocês empataram!')
elif m == 'Pedra' and mpc == 'Tesoura':
    print ('Você jogou Pedra e o computador jogou Tesoura, você venceu!')    
elif m == 'Pedra' and mpc == 'Papel':
    print ('Você jogou Pedra e computador jogou Tesoura, você perdeu!')
elif m == 'Papel' and mpc == 'Pedra':
    print ('Você jogou Papel e o computador jogou Pedra, você venceu!')
elif m == 'Papel' and mpc == 'Tesoura':
    print ('Você jogou Papel e o computador jogou Tesoura, você perdeu!')
elif m == 'Papel' and mpc == 'Papel':
    print ('Você jogou Papel e o computador jogou Papel, vocês empataram!')
elif m == 'Tesoura'and mpc == 'Pedra':
    print ('Você jogou Tesoura e o computador jogou Pedra, você perdeu!')
elif m == 'Tesoura' and mpc == 'Papel':
    print ('Você jogou Tesoura e o computador jogou Papel, você venceu!')
else:
    if m == 'Tesoura' and mpc == 'Tesoura':
        print ('Você jogou Tesoura e o computador jogou Tesoura, vocês empataram!')


        
'''                 .88888888:.
                88888888.88888.
              .8888888888888888.
              888888888888888888
              88' _`88'_  `88888
              88 88 88 88  88888
              88_88_::_88_:88888
              88:::,::,:::::8888
              88`:::::::::'`8888
             .88  `::::'    8:88.
            8888            `8:888.
          .8888'             `888888.
         .8888:..  .::.  ...:'8888888:.
        .8888.'     :'     `'::`88:88888
       .8888        '         `.888:8888.
      888:8         .           888:88888
    .888:88        .:           888:88888:
    8888888.       ::           88:888888
    `.::.888.      ::          .88888888
   .::::::.888.    ::         :::`8888'.:.
  ::::::::::.888   '         .::::::::::::
  ::::::::::::.8    '      .:8::::::::::::.
 .::::::::::::::.        .:888:::::::::::::
 :::::::::::::::88:.__..:88888:::::::::::'
  `'.:::::::::::88888888888.88:::::::::'
        `':::_:' -- '' -'-' `':_::::'`

------------------------------------------------
'''