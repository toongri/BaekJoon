def solution(rows, columns):
    answer = [[0] *columns for i in range(rows)]
    
    i = 0
    j = 0
    answer[i][j] = 1
    flag = True
    
    while(flag):

        preAnswer = answer[i][j]
        
        if preAnswer % 2 == 0:
            i = i + 1 if i != rows - 1 else 0
            if answer[i][j] != 0 and answer[i][j] % 2 == 1:
                return answer
            else:
                answer[i][j] = preAnswer + 1
        else:
            j = j + 1 if j != columns - 1 else 0
            if answer[i][j] != 0 and answer[i][j] % 2 == 0:
                return answer
            else:
                answer[i][j] = preAnswer + 1
        
        flag = False
        
        for r in range(rows):
            for c in range(columns):
                if answer[r][c] == 0:
                    flag = True
                    break
        print(answer)
    return answer

solution(3,3)