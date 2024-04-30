n = int(input())
arr = list(map(int, input().split()[:n]))
sorted_arr = sorted(arr)
indices = {value: index for index, value in enumerate(sorted_arr)}

for i in range(n):
    print(indices[arr[i]] + 1, end=" ")
