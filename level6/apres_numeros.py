#-*- encoding: utf-8 -*-
numeros = [0,0,0,0,0]
z = 0
while z < 5:
    numeros[z] = input('Número %d:' %(z+1))
    z+=1
while True:
    print('Digite 0 para sair')
    escolhido = input('Posição que você deseja imprimir: ')
    if escolhido == 0:
        break
    print('Você escolheu o número: %d' % (numeros[escolhido - 1]))
