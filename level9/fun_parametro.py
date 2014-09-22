def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def imprime(a,b,foper):
    print(foper(a,b))
imprime(3,4, soma)
imprime(14,2, subtracao)
