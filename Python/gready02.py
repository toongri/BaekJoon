x, y = map(int, input().split(" "))

arr = [0]*y


for i in range(x):
    arr[i] = list(map(int, input().split()))

rst = list(min(arr[i]) for i in range(x))

print(max(rst))