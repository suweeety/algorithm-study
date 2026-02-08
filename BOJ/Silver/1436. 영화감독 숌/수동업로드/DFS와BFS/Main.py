import sys
from collections import deque

input = sys.stdin.readline

# n, m, v 입력받기
n, m, v = map(int, input().split())

# 정점 담을 리스트 만들기
graph = [[] for _ in range(n+1)]

# 간선 넣어주기
for _ in range(n + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호 작은 것부터 방문
for i in range(n+1):
    graph[i].sort()

# 방문 체크
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

# dFS
def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in graph[v]: #2,3,4
        if not visited_dfs[i]:
            dfs(i)

# BFS
def bfs(v):
    visited_bfs[v] = True
    q = deque([v])
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]: #2,3,4
            if not visited_bfs[i]:
                visited_bfs[i] = True
                q.append(i)

dfs(v)
print()
bfs(v)