for tc in range(1, int(input())+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    # 갈 수 있는 곳 저장
    stack = []
    result = False
    visited = [[0] * N for _ in range(N)]
    start = 0
    end = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = i
                end = j
                visited[i][j] = 1
                stack.append(start)
                stack.append(end)
    for i in range(N):
        for j in range(N):
            while stack: # 스택이 있으면 돈다
                end = stack.pop()
                start = stack.pop()
                for k in range(4):
                    r = start + dx[k]
                    c = end + dy[k]
                    if 0 <= r < N and 0 <= c < N and visited[r][c] != 1:
                        temp = arr[r][c]
                        if temp == '0':
                            stack.append(r)
                            stack.append(c)
                            visited[r][c] = 1
                        elif temp == '3':
                            result = True
                            break
    if result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')