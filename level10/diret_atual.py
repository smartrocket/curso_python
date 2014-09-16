import os
os.chdir("x")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("y")
print(os.getcwd())
os.chdir("../z")
print(os.getcwd())
