n, k = map(int, input().split())

nlist = list()
arr = [10001] * 10001
arr[0] = 0

for i in range(n):
    nlist.append(int(input()))

for i in range(1, k + 1):
    for j in nlist:
        if i >= j:
            arr[i] = min(arr[i - j] + 1, arr[i])

print(arr[k])
