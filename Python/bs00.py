def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while(left<=right):
        mid = (left + right) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else : #mid < target
            left = mid + 1
    return -1


n = int(input())
nlist = list(map(int, input().split()))
p = int(input())
plist = list(map(int, input().split()))

nlist = sorted(nlist)

for i in plist:
    print(binarySearch(nlist, i))
    