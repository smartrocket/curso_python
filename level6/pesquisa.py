#-*- encoding: utf-8 -*-
Z = [4,12,16,24,32]
p = input('Valor a procurar:')
achou = False
y = 0
while y < len(Z):
    if Z[y] == p:
        achou = True
        break
    y += 1
if achou:
    print('%d encontrado na posição %d' %(p,y+1))
else:
    print('%d não encontrado' %p)
