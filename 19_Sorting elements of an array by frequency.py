# n = int(input())
# arr = list(map(int, input().split()[:n]))
# # 6
# # 1 3 2 1 2 2
# # 1 2 3
# # 2 2 2 1 1 3
#
# # arr.sort()
# a = list(set(arr))
# ct = {}
# for i in range(len(a)):
#     c = 0
#     for j in range(n):
#         if a[i] == arr[j]:
#             c = c + 1
#             ct[a[i]] = c
#
# dic = sorted(ct.items(), reverse=True, key=lambda item: item[1])
# for key, value in dic:
#     print(str(key) * value, end="")


# n = int(input())
# arr = list(map(int, input().split()[:n]))
#
# # Count occurrences of each element
# counter = {}
# for num in arr:
#     if num in counter:
#         counter[num] += 1
#     else:
#         counter[num] = 1
#
# # Sort the dictionary based on values
# sorted_counter = sorted(counter.items(), reverse=True, key=lambda item: item[1])
#
# # Print the elements sorted by their counts
# for key, value in sorted_counter:
#     print(str(key) * value, end="")


from collections import Counter

n = int(input())
arr = list(map(int, input().split()[:n]))

# Count occurrences of each element using Counter
counter = Counter(arr)

# Sort the dictionary based on values
sorted_counter = sorted(counter.items(), reverse=True, key=lambda item: item[1])

# Print the elements sorted by their counts
for key, value in sorted_counter:
    print(*([key] * value), end=" ")
