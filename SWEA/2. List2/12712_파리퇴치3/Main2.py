for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0

    # 십자가
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 대각선
    nx = [-1, 1, -1, 1]
    ny = [-1, -1, 1, 1]

    for i in range(n):
        for j in range(n):
            sum_v = arr[i][j]
            for k in range(4):
                for l in range(1, m):
                    r = i + dx[k] * l
                    c = j + dy[k] * l
                    if 0<=r<n and 0<=c<n:
                        sum_v += arr[r][c]
            
            sum2_v = arr[i][j]
            for k in range(4):
                for l in range(1, m):
                    r2 = i + nx[k] * l
                    c2 = j + ny[k] * l
                    if 0<=r2<n and 0<=c2<n:
                        sum2_v += arr[r2][c2]
            
            max_v = max(max_v, sum_v, sum2_v)

    print(f'#{tc} {max_v}')