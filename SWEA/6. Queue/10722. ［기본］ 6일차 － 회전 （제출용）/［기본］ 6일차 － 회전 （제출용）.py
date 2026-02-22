for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    Queue = list(map(int, input().split()))

    for i in range(M):
        Queue.append(Queue.pop(0))

    print(f'#{tc} {Queue.pop(0)}')