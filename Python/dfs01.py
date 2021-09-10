def dfs(x, y):
    visit[y][x] = False
    global arrNbh
    for ax, ay in arrNbh:
        px = ax + x
        py = ay + y
        if px >= 0 and py >= 0 and px < len(graph[0]) and py < len(graph):
            if visit[py][px] and not graph[py][px]:
                dfs(px, py)


y, x = map(int,input().split())
graph = [list(map(int, input())) for i in range(y)]
visit = [[True] * x for i in range(y)]
arrNbh = [(1,0), (0, 1), (-1, 0), (0, -1)]
cnt = 0

for i in range(y):
    for j in range(x):
        if visit[i][j] and not graph[i][j]:
            cnt+=1
            dfs(j, i)
print(cnt)