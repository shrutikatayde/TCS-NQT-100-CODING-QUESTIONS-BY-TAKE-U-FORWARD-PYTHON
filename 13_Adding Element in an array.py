n = int(input())
arr = []
print("original --> ", arr)
arr.insert(0, 1)
arr.insert(0, 3)
print("at begining --> ", arr)
arr.insert(n, 4)
print("at ending --> ", arr)
arr.insert(0, 5)
print("at begining --> ", arr)
arr.insert(n, 4)
print("at ending --> ", arr)
print("enter number where u want add element in an array: ")
ind = int(input())
value = int(input())
arr.insert(ind, value)
print("at specific position --> ", arr)
