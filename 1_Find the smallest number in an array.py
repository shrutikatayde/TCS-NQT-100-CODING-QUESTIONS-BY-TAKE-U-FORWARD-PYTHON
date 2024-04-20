def small_num(n, arr):
    min = arr[0]
    for i in range(1, n):
        if arr[i]<min:
            min = arr[i]
    return min
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        x = int(input())
        arr.append(x)
    res = small_num(n, arr)
    print(res)
