import time
import numpy as np

start = time.time()
#1번
"""
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

answer is shirt
"""


#2번

"""
a = 1000//3+1

result = list(b * 3 for b in range(1,a))
print(sum(result))

i = 0
c = 0
while(i<a):
    c += 3*i
    i+=1

print(c)


"""

#3번

"""
i=1
j=5

while(i<=j):
    print("*"*i)
    i+=1

"""

#4번
"""
for i in range(1, 101):
    print(i)
print(list( i for i in range(1,101)]))

"""

#5번

"""
arr = list(70, 60, 55, 75, 95, 90, 80, 80, 85, 100)

print(sum(arr)/len(arr))

arr = list(70, 60, 55, 75, 95, 90, 80, 80, 85, 100)

print(np.array(arr).mean())

"""

#6번
"""
result = list(n*2 for n in range(1,6) if n % 2 ==1)

print(result)
"""
"""
car_num = [ [1011, 1022], [1201, 7202], [2301, 1302] ]

for a, b in car_num:
    print("차량번호 ", a)
    print("----")
    print("차량번호 ", b)
    print("----")
"""
"""
car_num = [ [1011, 1022], [1201, 7202], [2301, 1302] ]
for i in (0,1,2):
  for j in (0,1):
    print("차량번호", car_num[i][j])
    print("-----")
"""
#d = dict()
#for i in range(2,10):
#    d[i] = list(i*j for j in range(1,10))
#print(d)

d = dict()
for i in range(2,10):
    l = list()
    for j in range(1,10):
        l.append(i*j)
    d[i]=l
print(d)

#d = {i : list(i*j for j in range(1,10)) for i in range(2,10)}
#print(d)

#print({i : list(i*j for j in range(1,10)) for i in range(2,10)})

end = time.time()
print(end-start)