def binarySearch(array, target, start, end):
    while start >= end:
        mid = (start + end) / 2

        if mid == target:
            return mid
        elif mid > target:
            start = mid + 1
        else : #elif mid < target
            end = mid - 1
        
    return None

