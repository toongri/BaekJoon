# index / 0 : 2번째로 입력되는 입력의 길이, 1 : 총 계산 횟수 , 2 : 허용되는 연속되는 계산의 값
print("와쌉")
que = list(map(int, input().split()))

arr = list(map(int, input().split()))

arr.sort()

if arr[-1] == arr[-2]:          # 최댓값이 두개 이상이면 que[2] 값과 무관하게 반복하면 된다.
    print(arr[-1] * que[1])
else:                           # 최댓값이 한개라면 최대값*허용치 + 두번째값*1 을 반복하면 된다.
    ahrt = que[1] // (que[2] + 1)
    skaj = que[1] % (que[2] + 1)
    print(arr[-1] * (ahrt * que[2] + skaj) + arr[-2] * ahrt)