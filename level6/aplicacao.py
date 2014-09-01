lista_inic = [7,10,5,14,0,11,23]
par = []
impar = []
for e in lista_inic:
    if e % 2 == 0:
        par.append(e)
    else:
        impar.append(e)
print 'Pares: ', par
print 'Impares: ', impar
