def find(i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for k in range(4):
        for l in range(1, n):
            r = i + dx[k] * l
            c = j + dy[k] * l
            # 주변에 작은게 있으면 넣어.
            if 0 <= r < n and 0 <= c < n:
                if arr[r][c] > 0:
                    break
                else:
                    arr[r][c] = 3

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                find(i, j)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')