lista = [6,5,3,4,7,1,8,2]
changed = True
while changed:
    changed = False
    for i in xrange(len(lista) - 1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
            changed = True
print(lista)
