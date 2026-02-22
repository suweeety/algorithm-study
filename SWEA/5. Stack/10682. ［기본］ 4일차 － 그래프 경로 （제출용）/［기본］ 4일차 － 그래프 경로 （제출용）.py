for tc in range(1, int(input())+1):
    V, E = map(int, input().split()) # 노드와 간선

    arr = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)

    S, G = map(int, input().split()) # 출발노드와 도착노드

    visited = [False] * (V+1)
    stack = [S]
    result = 0

    while stack: # 스택이 없으면 끝남
        now = stack.pop()

        if now == G:
            result = 1
            break
        if not visited[now]:
            visited[now] = True

            for w in arr[now]:
                if not visited[w]:
                    stack.append(w)

    print(f'#{tc} {result}')