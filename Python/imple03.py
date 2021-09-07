a , b = input()
n = 8
a = ord(a)-97
b = int(b)-1

cnt = 0

arr = [ (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1) ]

for i, j in arr:
    px = b + j
    py = a + i
    if px < n and px >= 0 and py < n and py >= 0:
        cnt += 1

print(cnt)