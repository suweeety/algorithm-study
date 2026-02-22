from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    # -1은 방문안한 상태 / 0은 방문함 / 1은 거리 카운팅!
    start_i, start_j = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i, start_j = i, j
                visited[i][j] = 0
                break
        if start_i != -1: break
    
    def bfs(i, j):
        q = deque()
        q.append((i, j))
        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if maze[nr][nc] == 3:
                        return visited[r][c]
                    if maze[nr][nc] == 0 and visited[nr][nc] == -1:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1
        return 0

    print(f'#{tc} {bfs(start_i, start_j)}')