from collections import deque

# v: 과목 수, E: 선수 관계 수
# graph: 인접 리스트, indegree: 선수과목 개수 배열

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    data = list(map(int, input().split()))
    
    # 초기화
    adj = [[] for _ in range(v + 1)]
    degree = [0] * (v + 1)

    # 간선
    for i in range(0, len(data), 2):
        a, b = data[i], data[i+1]
        adj[a].append(b)
        degree[b] += 1

    queue = deque()
    # 진입차수 0부터 시작
    for i in range(1, v + 1):
        if degree[i] == 0:
            queue.append(i)
    
    ans = 0
    while queue:
        ans += 1
        for _ in range(len(queue)):
            temp = queue.popleft()
            for i in adj[temp]:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)

    print(f'#{tc} {ans}')