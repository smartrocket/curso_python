#-*- encoding: utf-8 -*-
def par(a):
    return(a%2==0)
def par_impar(a):
    if par(a):
        return "Par"
    else:
        return "Ímpar"
print(par_impar(8))
print(par_impar(3))
