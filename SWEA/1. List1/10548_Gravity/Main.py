for tc in range(1, int(input())+1):
    pass
    n = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    for i in range(len(arr)):
        cnt = 0
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                cnt+=1
        if max_v < cnt:
            max_v = cnt
    
    print(f'#{tc} {max_v}')