#-*- encoding: utf-8 -*-
x = input('Informe o primeiro valor: ')
y = input('Informe o segundo valor: ')
if x > y:
    aux = x
    x = y
    y = aux
print ('Números na ordem crescente: %d %d' %(x, y))

