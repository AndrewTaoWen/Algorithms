def check(a,b):
    if a > b:
        return(GCF(a,b))
    else:
        return(GCF(b,a))

def GCF(a,b):
    if b == 0:
        return a
    # elif a > b:
    #     return GCF(a % b, b)
    else:
        return GCF(b, a % b)

print(check(192, 270))