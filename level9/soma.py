#-*- encoding: utf-8 -*-
import calculus

l = []
for i in range(10):
    l.append(input("Digite um numero: "))
print "Total", calculus.soma_inteiros(*l)
