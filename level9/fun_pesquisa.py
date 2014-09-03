def pesquisa(lista, valor):
    for n,e in enumerate(lista):
        if e == valor:
            return n
    return None
l = [5, 10, 15, 20]
print(pesquisa(l, 15))
print(pesquisa(l, 23))
