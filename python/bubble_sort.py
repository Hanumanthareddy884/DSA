
list = [86, 7, 5, 6, 8, 5, 1, 25, 3]
for i in range(len(list)):
    for j in range(len(list)):
        if list[j]>list[i]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list,end=" ")