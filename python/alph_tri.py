import string
lower = list(string.ascii_uppercase)

for i in range(5):
    for j in range(5,i,-1):
        print(lower[i],end=" ")

    print()