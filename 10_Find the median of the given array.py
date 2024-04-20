n = int(input())
arr = list(map(int, input().split()[:n]))

arr.sort()
if n % 2 != 0:
    print(arr[n // 2])
else:
    prev = arr[(n // 2) - 1]
    nex = arr[n // 2]
    print((prev + nex) / 2)
