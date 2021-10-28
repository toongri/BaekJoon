def quicksort(array, start, end):
    if start >= end:
        return
    point = start
    left = start+1
    right = end
    while(left <= right):
        while left <= end and array[left] <= array[point]:
            left += 1
        while array[right] >= array[point] and right > start:
            right -= 1
        if left > right:
            array[point], array[right] = array[right], array[point]
        else:
            array[left], array[right] = array[right], array[left]

    
    quicksort(array, start, right - 1)
    quicksort(array, right + 1, end)

arr = [5, 4, 3, 2, 1]

print(arr)
quicksort(arr, 0, 4)
print(arr)