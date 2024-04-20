if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    arr.sort()
    temp_arr = []
    for i in range(n//2, n):
        temp_arr.append(arr[i])
    temp_arr.sort(reverse=True)
    final = arr[:len(arr)//2 ]+ temp_arr
    for i in range(n):
        print(final[i], end=' ')