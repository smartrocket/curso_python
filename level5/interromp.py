#-*- encoding: utf-8 -*-
soma = 0
print('Digite 0 para sair')
while True:
    n = input('Digite o número que deseja somar: ')
    if (n == 0):
        break
    soma = soma + n
print('Soma: %d' %soma)
