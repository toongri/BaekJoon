def binarySearch(arr, target):
    left = 0
    right = max(arr)

    while(left <= right):
        mid = (left + right) // 2
        b = listCut(arr, mid)
        if b == target:
            return mid
        elif b > target:
            left = mid + 1
        elif b < target:
            right = mid - 1
    return -1

def listCut(arr, cut):
    sum = 0
    for i in arr:
        a = i - cut
        if a > 0:
            sum += a
    return sum

n, k = map(int, input().split())

arr = list(map(int, input().split()))

print(binarySearch(arr, k))