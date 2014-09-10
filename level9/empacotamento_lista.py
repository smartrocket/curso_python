def barra(n=8,c="*"):
    print(c*n)
l = [[5,"-"],[10,"*"],[5],[6,"."]]
for e in l:
    barra(*e)
