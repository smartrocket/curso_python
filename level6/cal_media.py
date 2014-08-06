#-*- encoding: utf-8 -*-
notas = [5,6,8,7,9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x+=1
print('Média: %.2f' %(soma/x))
