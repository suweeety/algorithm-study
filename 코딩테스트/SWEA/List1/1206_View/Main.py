for tc in range(1, 11):
    pass
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n-2):
        neighbors = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        neighbors_max = max(neighbors)
        if arr[i] > neighbors_max:
            cnt += arr[i] - neighbors_max

    print(f'#{tc} {cnt}')