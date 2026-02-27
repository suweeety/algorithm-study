def dfs():
    visited = [0] * 100 # 방문처리 (정점 0~99)
    visited[0] = 1      # 시작점(0)
    stack = [0]         # 시작

    while stack:
        v = stack.pop()

        if v == 99:     # 목적지에 도착했다면
            return 1

        for i in adj[v]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
    return 0

for _ in range(1, 11):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(100)]

    for i in range(0, len(arr), 2):
        adj[arr[i]].append(arr[i+1])

    result = dfs()
    print(f'#{T} {result}')