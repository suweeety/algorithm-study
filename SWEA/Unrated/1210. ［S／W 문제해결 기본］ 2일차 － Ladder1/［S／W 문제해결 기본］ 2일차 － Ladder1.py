for _ in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    visited = [[False] * 100 for _ in range(100)]

    # 좌, 우, 상
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    stack = []

    st_i, st_j = 0, 0
    for i in range(100):
        if arr[99][i] == 2:
            st_i, st_j = 99, i
            break

    stack = [(st_i, st_j)]
    visited[st_i][st_j] = True

    result = 0
    while stack:
        r, c = stack.pop()

        if r == 0:
            result = c
            break

        for k in range(3):
            nr = r + dx[k]
            nc = c + dy[k]

            if 0 <= nr < 100 and 0 <= nc < 100:
                if arr[nr][nc] == 1 and not visited[nr][nc]:
                    stack.append((nr, nc))
                    visited[nr][nc] = True
                    break

    print(f'#{T} {result}')