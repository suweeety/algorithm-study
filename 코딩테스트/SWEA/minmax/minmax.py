T = int(input())

for test_cace in range(1, T+1): # tc 테스트케이스 번호
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = arr[0]

    # 최댓값 찾기
    # 나머지 모든 원소 arr[i]와 비교
    for i in range(N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]

    print(f'#{test_cace} {max_v - min_v}')