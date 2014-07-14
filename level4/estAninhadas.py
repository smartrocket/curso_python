#-*- encoding: utf-8 -*-
minutos = input('Minutos utilizados no mês: ')
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print('Conta do celular: R$ %.2f' %(minutos * preco))
