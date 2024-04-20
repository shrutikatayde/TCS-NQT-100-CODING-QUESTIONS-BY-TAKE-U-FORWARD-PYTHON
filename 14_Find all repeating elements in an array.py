arr = list(map(int, input().split()))
le = len(arr)
op_Arr = []

# Traverse the array and append duplicates to op_Arr
for i in range(le - 1):
    for j in range(i + 1, le):
        if arr[i] == arr[j]:
            op_Arr.append(arr[i])
print(op_Arr)
