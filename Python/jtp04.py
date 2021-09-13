import numpy as np

"""
def is_odd(a):
    return a%2 == 1

print(is_odd(1))

"""

"""
print(np.mean(list(map(int, input().split()))))
"""

"""
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

print(int(input1) + int(input2))
"""
"""
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
3번
"""
"""
f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

"""
"""
f = open('test.txt', 'a')
f.write(input("글:")+"\n")
f.close()
"""
"""
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
"""