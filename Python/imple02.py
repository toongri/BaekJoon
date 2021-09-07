arr = [0, 60, 60]

arr[0] =int(input())+1

cnt = 0

for i in range(arr[0]):
    for j in range(arr[1]):
         for k in range(arr[2]):
             if '3' in str(i)+str(j)+str(k):
                 cnt += 1
print(cnt)