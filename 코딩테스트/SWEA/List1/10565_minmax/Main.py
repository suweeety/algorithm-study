for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))

    max_value = arr[0]
    min_value = arr[0]

    for i in range(1, n):
        if max_value < arr[i]:
            max_value = arr[i]
        if min_value > arr[i]:
            min_value = arr[i]
    
    print(f'#{tc} {max_value - min_value}')