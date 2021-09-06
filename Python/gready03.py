a, b = map(int, input().split(" "))

cnt = 0
while(a >= b):
    cnt += a % b + 1                                             
    a = a // b

print(cnt + a - 1)