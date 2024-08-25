def fac(n):
    if(n==0):
        return 1
    a= n*fac(n-1)
    return a

print(fac(5))