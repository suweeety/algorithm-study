for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    Queue = []
    for i in range(N):
        Queue.append((i, arr[i]))
    next_i = N
    while len(Queue) > 1:
        idx, ch = Queue.pop(0)
        if (ch // 2) > 0:
            Queue.append((idx, (ch // 2)))
        elif next_i < M:
            Queue.append((next_i, arr[next_i]))
            next_i += 1

    result_idx, result = Queue.pop(0)
    print(f'#{tc} {result_idx+1}')