'''
1. 아아이디어
- 2중 for문 => 값이 1 && 방문 X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- v : 500 * 500
- E : 4 * 500 * 500
- V + E : 5 * 250000 = 1000000 < 2억 => 가능!

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
'''

import sys
from collections import deque # 큐 기능을 쓰기 위해 가져온다.

input = sys.stdin.readline # 입력을 더 빠르게 처리하는 함수로 바꾼다

# 도화지의 세로(n)와 가로(m) 크기를 입력받는다
n, m = map(int, input().split())

# 도화지 정보를 한 줄씩 읽어서 2차원 리스트(행렬)로 만든다.
graph = [list(map(int, input().split())) for _ in range(n)]

# 방문했는지 체크할 '똑같은 크기의 도화지'를 만들고 전부 False(안갔음)로 채운다
visited = [[False] * m for _ in range(n)]

# 2. BFS 핵심 엔진(그림의 넓이 구하기 함수)
# 방향 벡터 (우, 하, 좌, 상)
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    rs = 1 # 그림의 넓이를 저장할 변수 (시작점 포함이므로 1)
    q = deque([(y, x)]) # 큐 생성 및 시작점 삼입 (popleft를 위해 deque 사용)
    
    while q:
        ey, ex = q.popleft() # 큐의 맨 앞을 꺼냄(가장 먼저 들어온 것)
        
        for k in range(4): # 4방향 검사
            ny = ey + dy[k]
            nx = ex + dx[k]

            # 도화지 범위 안에 있고
            if 0 <= ny < n and 0 <= nx < m:
                # 그림 1이면서 아직 방문 안했다면
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    rs += 1 # 넓이 1 증가
                    visited[ny][nx] = True # 방문 표시 (큐에 넣을 때 바로!)
                    q.append((ny. nx)) # 다음 탐색 후보로 큐에 추가
    return rs # 측정이 끝난 그림의 넓이 반환

cnt = 0 # 그림 개수
maxv = 0 # 최대 넓이

# 도화지를 한 칸씩 순회
for j in range(n):
    for i in range(m):
        # 그림을 발견했는데 아직 방문안한곳이라면?
        if graph[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            cnt += 1 # 그림 개수 +1
            maxv = max(maxv, bfs(j,i)) # BFS로 넓이 구해와서 최댓값 갱신

print(cnt)
print(maxv)