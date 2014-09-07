#-*- encoding: utf-8 -*-
x = 4
def muda_e_imprime():
    global x
    x = 8
    print("x dentro da função: %d" % x)
print("x antes de mudar: %d" % x)
muda_e_imprime()
print("x depois de mudar: %d" % x)
