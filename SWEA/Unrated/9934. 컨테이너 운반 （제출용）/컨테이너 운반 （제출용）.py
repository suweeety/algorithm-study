T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))

    weight.sort(reverse=True)
    capacity.sort(reverse=True)

    total = 0
    w_idx = 0
    c_idx = 0

    while w_idx < N and c_idx < M:
        if weight[w_idx] <= capacity[c_idx]:
            total += weight[w_idx]
            w_idx += 1
            c_idx += 1
        else:
            w_idx += 1

    print(f'#{tc+1} {total}')