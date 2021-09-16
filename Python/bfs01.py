from collections import deque

arrVec = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def bfs(arrGrp, staX, staY, arrVst):
    queue = deque([(staX, staY)])
    global arrVec, a, b

    arrVst[staY][staX] = 1

    while(queue):
        x, y = queue.popleft()

        for ix, iy in arrVec:
            px = x + ix
            py = y + iy

            if(px < b and px >= 0 and py < a and py >= 0):
                if(arrVst[py][px] == 0 and arrGrp[py][px] == True):
                    queue.append((px, py))
                    arrVst[py][px] = arrVst[y][x] + 1

    print(arrVst[a - 1][b - 1])
    return 0


a, b = map(int, input().split())

arrGrp = [list(map(int, input())) for i in range(a)]

arrVst = [[0] * b for i in range(a)]

bfs(arrGrp, 0, 0, arrVst)
