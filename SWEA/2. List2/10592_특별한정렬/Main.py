T = int(input())
for tc in range(1, T+1):
    pass
    # k 찾기,
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = []
    arr.sort()
    # 왼쪽에서 2번 오른쪽 2번
    for i in range(5):
        pass
        la = arr.pop()
        new_arr.append(la)
        r = arr.pop(0)
        new_arr.append(r)
 
    print(f'#{tc}', *new_arr)