for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    status = False
    
    # 갈 수 있는 곳 저장
    stack = []
    visited = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                si, sj = i, j
                stack.append((si, sj))

    while stack: # 스택이 있으면 돈다
        x, y = stack.pop()
        for k in range(4):
            r = si + dx[k]
            c = sj + dy[k]
            if 0 <= r < N and 0 <= c < N:
                if maze[r][c] == '0':
                    stack.append((r, c))
                    maze[r][c] = 4
                if maze[r][c] == '3':
                    status = True
                    break
    if status:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')