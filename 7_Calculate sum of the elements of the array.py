if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    sum = 0
    # print(sum(arr))
    for i in arr:
        sum += i
    print(sum)
