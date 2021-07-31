print('')
print('====== JOGO DA ADIVINHAÇÃO ======')
print('')
from random import randint
from time import sleep
print('''Vamos brincar!!!
Eu vou escolher um número entre 1 e 10
e você terá que advinhar que número é esse.''')
n1=randint(1, 10)
n2=int(input('Escolha o seu número: '))
print('PROCESSANDO...')
sleep(1)
tenta=0
while not n1 == n2:
    if n1 != n2:
        print('Erroooou!!! Tente novamente')
        n2=int(input('Escolha outro número: '))
        tenta+=1
        print('PROCESSANDO...')
        sleep(1)
    if n1 == n2:
        print('ACEEERTOOOU!!! Você escolheu {} e o computador escolheu {}.'.format(n2,n1))
        tenta+=1
        sleep(1)
print('Parabéns você acertou na {}ª tentativa.'.format(tenta))