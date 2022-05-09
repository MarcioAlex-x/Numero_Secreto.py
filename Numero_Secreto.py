from random import randint
from time import sleep


print('\033[1;34m ='*13)
print('\033[1;34m --== Número Secreto ==--')
print('\033[1;34m ='*13)
sleep(1)
print('\n\033[1;30mVocê precisa acertar o número secreto que está '
      '\033[1;32m entre 0 e 100!\n\033[1;30m Boa sorte!\n  \n')

numero_secreto = random.randint(1,100)
chances = 0
chute = 0
print(numero_secreto)

while chute != numero_secreto and chances < 3:
    sleep(2)
    chute = int(input('\033[1;30mAgora tente acertar o número secreto: '))

    if chute == numero_secreto:
        sleep(.7)
        print('\033[1;32mParabéns, você acertou')
        break
    elif chute < numero_secreto:
        sleep(.7)
        print('\033[1;31mVocê errou! \033[1;33mO número secreto é maior')
    elif chute > numero_secreto:
        sleep(.7)
        print('\033[1;31mVocê errou! \033[1;33mO número secreto é menor')

    chances+=1
    sleep(.7)
print('\033[1;30mFim de jogo!')