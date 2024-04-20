n = int(input())
arr = list(map(int, input().split()[:n]))

# print(set(arr))
arr.sort()
prev = 0
i = 1
while i < n:
    if arr[prev] != arr[i]:
        prev += 1
        arr[prev] = arr[i]
    i += 1
print(arr[: prev + 1])
