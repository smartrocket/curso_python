#-*- encoding: utf-8 -*-
compras = []
while True:
    item = raw_input("Item: ")
    if item == "fim":
        break
    compras.append(item)
for p in compras:
    print(p)
