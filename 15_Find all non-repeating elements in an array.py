arr = list(map(int, input().split()))
le = len(arr)

for i in range(le):
    boolean = False
    for j in range(le):
        if i != j and arr[i] == arr[j]:
            boolean = True
            break
    if boolean != True:
        print(arr[i])
