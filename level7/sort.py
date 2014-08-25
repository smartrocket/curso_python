Lista = [6,5,3,4,7,1,8,2]
end = 8
while end > 1:
    changed = False
    x = 0
    while x < (end-1):
        if Lista[x] > Lista[x+1]:
            changed = True
            aux = Lista[x]
            Lista[x] = Lista[x+1]
            Lista[x+1] = aux
        x += 1
    if not changed:
        break
    end -= 1
for e in Lista:
    print(e)
