for tc in range(1, int(input())+1):
    pass
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    find_arr = list(map(int, input().split()))
    
    cnt = 0
    start = 0
    end = n
    for i in range(m):
        for j in range(start, end):
            if find_arr[i] == arr[j]:
                cnt += 1
                start = j
                break
    if cnt == m:
        print(f'#{tc} {cnt} {m} YES')
    else:
        print(f'#{tc} {cnt} {m} NO')