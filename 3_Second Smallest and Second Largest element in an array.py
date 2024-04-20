if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()[:n]))

    # Initialize second smallest and second largest
    second_min = float('inf')
    second_max = float('-inf')

    min = float('inf')
    max = float('-inf')

    # Find second smallest and second largest
    for num in arr:
        if num < min:
            second_min = min
            min = num
        elif num < second_min and min != num:
            second_min = num

        if num > max:
            second_max = max
            max = num

    # Remove duplicates
    arr = list(dict.fromkeys(arr))

    # Check if array has less than 2 unique elements
    if len(arr) < 2:
        print("Array has less than 2 unique elements.")
    else:
        print(f"Second smallest element: {second_min}")
        print(f"Second largest element: {second_max}")