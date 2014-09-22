multiplos = open("multiplos de 4.txt","w")
pares = open("pares.txt")
for l in pares.readlines():
    if int(l) % 4 == 0:
        multiplos.write(l)
pares.close()
multiplos.close()
