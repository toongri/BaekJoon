n = int(input())
nlist = list(map(int, input().split()))

list = [0] * 100

list[0] = nlist[0]
list[1] = max(nlist[0], nlist[1])

for i in range(2, len(nlist)):
    list[i] = max(list[i - 1], list[i - 2] + nlist[i])

print(list[n - 1])