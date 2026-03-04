def onoff(i):
    for i in range(i, n):
        if tobe[i] == 0:
            tobe[i] = 1
        else:
            tobe[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    asis = list(map(int, input().split()))
    tobe = list(map(int, input().split()))
    res = 0
    for i in range(n):
        if asis[i] != tobe[i]:
            onoff(i)
            res += 1

    print(f'#{tc} {res}')