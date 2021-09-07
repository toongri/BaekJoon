a = int(input())

b = list(input().split(" "))

c = [1,1]

for i in b:

    if i == 'R':
        if c[1] < a:
            c[1] += 1;
    elif i == 'L':
        if c[1] > 1:
            c[1] -= 1;
    elif i == 'U':
        if c[0] > 1:
            c[0] -= 1;
    elif i == 'D':
        if c[0] < a:
            c[0] += 1;

print(c[0], c[1])