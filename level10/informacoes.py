import os
import os.path
import time
import sys
nome = sys.argv[0]
print("Nome: %s" % nome)
print("Tamanho: %d" % os.path.getsize(nome))
print("Criado: %s" % time.ctime(os.path.getctime(nome)))
print("Modificado: %s" % time.ctime(os.path.getctime(nome)))
print("Acessado: %s" % time.ctime(os.path.getatime(nome)))
