import os
import sys
for raiz, diretorios,arquivos in os.walk(sys.argv[1]):
    print("\nCaminho:", raiz)
    for d in diretorios:
        print(" %s/" % d)
    for f in arquivos:
        print(" %s" % f)
    print("%d diretorio(s), %d arquivos(s)" % (len(diretorios), len(arquivos)))
