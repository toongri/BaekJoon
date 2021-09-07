def turnDirect():
    global usrDir
    global cntTrn
    cntTrn += 1
    usrDir = 3 if usrDir == 0 else usrDir - 1


y, x = map(int, input().split(" "))

usrX, usrY, usrDir = map(int, input().split(" "))

arrSea=[]
for i in range(y):
    arrSea.append(list(map(bool, map(int, input().split(" ")))))

arrChk = []

arrChk = [[False] * x for i in range(y)]

arrDir = [[-1, 0, 1, 0], [0, 1, 0, -1]]

cntLod = 1
cntTrn = 0
arrChk[usrX][usrY] = True

while(True):
    turnDirect()
    
    py = usrY + arrDir[0][usrDir]
    px = usrX + arrDir[1][usrDir]

    if arrChk[py][px] == False and arrSea[py][px] == False:
        usrY = py
        usrX = px
        cntTrn = 0
        cntLod += 1
        arrChk[py][px] = True

    else:
        if cntTrn > 3:
            py = usrY - arrDir[0][usrDir]
            px = usrX - arrDir[1][usrDir]

            if arrSea[py][px] == True:
                break
            else:
                usrY = py
                usrX = px
                cntTrn = 0

print(cntLod)



