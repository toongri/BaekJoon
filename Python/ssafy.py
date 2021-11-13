from itertools import combinations

arr = [5,9,7,11,3,4,1,10,8]

rst = list(map(list, combinations(arr, 2)))
    

arr1 = []
arr2 = arr[:]

resultInt = 0

for rst_index in rst:
    arr1 = []
    arr2 = arr[:]
    for i in rst_index:
        arr2.remove(i)
        arr1.append(i)
    arr2 = list(map(int, arr2))
    arr1 = list(map(int, arr1))
    compare = max(arr2) + max(arr1) - min(arr2) - min(arr1)
    resultInt = max(compare, resultInt)
    
print(resultInt)