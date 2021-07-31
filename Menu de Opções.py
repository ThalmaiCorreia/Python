print('')
print('====== MENU DE OPÇÕES ======')
print('')
n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
e=0
while e != 5:
    print('''ESCOLHA A OPÇÃO DESEJADA
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    e=int(input('>>>>>> OPÇÃO: '))
    if e == 1:
        print('A soma entre {} + {} = {}.'.format(n1,n2,n1+n2))
    elif e == 2:
        print('A multiplicação entre {} x {} = {}.'.format(n1,n2,n1*n2))
    elif e == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior valor é {}.'.format(n1,n2,n1))
        else:
            print('Entre {} e {}, o maior valor é {}.'.format(n1,n2,n2))
    elif e == 4:
        print('Informe os números novamente!')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
    elif e == 5:
        print('Finalizando...')
    else:
        print('OPÇÃO INVÁLIDA!!')
    print('='*20)
print('Fim do programa! Volte Sempre!')