#-*- encoding: utf-8 -*-
lista = [1,7,14,28,56]
n = input('Digite o número a pesquisar: ')
for i in lista:
    if i == n:
        print('Número encontrado!')
        break
else:
    print('Número não encontrado')
