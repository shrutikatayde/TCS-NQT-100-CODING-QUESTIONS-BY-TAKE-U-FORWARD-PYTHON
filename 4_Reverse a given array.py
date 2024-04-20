n = int(input())
arr = list(map(int, input().split()[:n]))

start = 0
end = -1
for _ in range(n//2):
    arr[start], arr[end] = arr[end], arr[start]
    start+=1
    end-=1
print(arr)