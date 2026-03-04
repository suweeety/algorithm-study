for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    res = 0
    arr_c = []
    for i in range(max(n, m)):
        if arr_a:
            arr_c.append(arr_a.pop(0))
        if arr_b:
            arr_c.append(arr_b.pop(0))

    print(f'#{tc}', *arr_c)