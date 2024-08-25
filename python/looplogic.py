n = 6
for i in range(1, n+1):
    print(i,end=" ")
    a = i
    for j in range(n, i, -1):
        a += j
        print(a, end=" ")
    print()
