for tc in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0
    for _ in range(dump):
        for i in range(len(arr)):
            if arr[max_idx] < arr[i]:
                max_idx = i
            if arr[min_idx] > arr[i]:
                min_idx = i
        
        if (arr[max_idx] - arr[min_idx]) <= 1:
            break
        
        arr[max_idx] -= 1
        arr[min_idx] += 1
    final_max = max(arr)
    final_min = min(arr)

    print(f'#{tc} {final_max - final_min}')