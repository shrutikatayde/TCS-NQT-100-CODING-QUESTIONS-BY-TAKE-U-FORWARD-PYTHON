n = int(input())
arr = list(map(int, input().split()[:n]))
uniq_arr=list(set(arr))
# print(uniq_arr)

for i in range(len(uniq_arr)):
    count = 0
    for j in range(n):
        if uniq_arr[i]==arr[j]:
            count+=1
    print(uniq_arr[i], count)