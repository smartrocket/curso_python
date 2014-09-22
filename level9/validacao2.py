#-*- encoding: utf-8 -*-
def faixa_int(pergunta, minimo, maximo):
    while True:
        x = input((pergunta))
        if x < minimo or x > maximo:
            print("Valor inválido. Digite um valor entre %d e %d" % (minimo,maximo))
        else:
            return x
