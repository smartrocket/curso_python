def soma(*args):
    s=0
    for x in args:
        s+=x
    return s
print soma(2,2)
print soma(6)
print soma(4,2,1,4)
print soma(9,10,3,2,1,8,7)
