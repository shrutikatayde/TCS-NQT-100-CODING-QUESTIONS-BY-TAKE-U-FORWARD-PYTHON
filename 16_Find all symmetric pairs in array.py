def findPairs(arr):
    # Create an empty set to store pairs
    s = set()

    # Iterate through the array to find mirror pairs
    for pair in arr:
        x, y = pair

        # Insert the current pair `(x, y)` into the set
        s.add((x, y))

        # Check if mirror pair `(y, x)` is seen before, print the pairs
        if (y, x) in s:
            print(f"({x}, {y})")


# Taking input from the user
n = int(input("Enter the number of pairs: "))
arr = []
print("Enter the pairs (format: x y): ")
for _ in range(n):
    pair = tuple(map(int, input().split()))
    arr.append(pair)

# Find and print mirror pairs
print("The mirror pairs are:")
findPairs(arr)
