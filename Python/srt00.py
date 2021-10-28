def sort():
    global inputArr, arr
    for i in range(len(inputArr)):
        for j in range(len(arr)):
            if inputArr[i] >= arr[j]:
                arr.insert(j, inputArr[i])
                break
            else:
                if j+1 == len(arr):
                    arr.append(inputArr[i])
arr=[]

i=input()

inputArr=[input() for j in range(int(i))]

arr.append(inputArr.pop(0))

sort()

print(arr)
