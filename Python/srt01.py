

inp = int(input())

list = [input().split() for i in range(inp)]



list = sorted(list, key = lambda data: int(data[1]))

print(list)