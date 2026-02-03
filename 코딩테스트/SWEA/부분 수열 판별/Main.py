for tc in range(int(input)):
    # 정수 A, B 의 길이 입력받기
    N, M = map(int, input().split())
    # 정수 A, B 길이만큼 A, B 입력받기
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    curr = 0
    for i in range(N):
        if curr < M and A[i] == B[curr]:
            curr += 1