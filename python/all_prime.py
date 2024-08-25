n = int(input("Enter value = "))
all_prime = [2]

for i in range(1,n):
    for j in range(2,i):
        if i % j ==0:
            break
        elif j ==i-1:
            all_prime.append(i)

print(all_prime)
