if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    k = int(input())

    # print(arr[k:] + arr[:k])

    t_arr = []
    for i in range(k):
        t_arr.append(arr[i])

    print(arr[k:] + t_arr)
