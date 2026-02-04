T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max = 0
    for i in range(N):
        count = 0
        
        for j in range(i, N):
            if arr[i] > arr[j]:
                count += 1
        if max < count:
            max = count

    print(f'#{tc+1} {max}')