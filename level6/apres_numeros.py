#-*- encoding: utf-8 -*-
numeros = [0,0,0,0,0]
x = 0
while x < 5:
    numeros[x] = input('Número %d: ' %(x + 1))
    x += 1
while True:
    print('Digite 0 para sair')
    escolhido = input('Posição que você deseja imprimir: ')
    if (escolhido == 0):
        break
    print('Você escolheu o número: %d' %(numeros[escolhido - 1]))
