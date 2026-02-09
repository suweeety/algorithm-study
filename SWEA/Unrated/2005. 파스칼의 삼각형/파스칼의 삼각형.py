for tc in range(1, int(input())+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    print(f'#{tc}')
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    
        row = [str(k) for k in arr[i] if k != 0]
        print(*row)