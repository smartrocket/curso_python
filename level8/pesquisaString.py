#-*- encoding: utf-8 -*-
s = "ana banana"
p = 0
while (p > -1):
    p = s.find("ana", p)
    if p >= 0:
        print("Posição: %d" %p)
        p+=1
