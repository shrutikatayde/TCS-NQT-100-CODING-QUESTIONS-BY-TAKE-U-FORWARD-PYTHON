n = int(input())
arr = list(map(int, input().split()[:n]))

max_pro = float("-inf")  # Initialize max_pro with negative infinity

for i in range(n):
    pro = 1
    for j in range(i, n):
        pro = pro * arr[j]
        if pro > max_pro:
            max_pro = pro

# print(max_pro)
print(max(max_pro, pro))
