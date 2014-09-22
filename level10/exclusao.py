import os
# Cria um arquivo e o fecha imediatamente
open("exclusao.txt","w").close()
os.mkdir("vazio")
os.rmdir("vazio")
os.remove("exclusao.txt")
