T = int(input())
 
for tc in range(1, T+1):
    # N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
    N, M = map(int, input().split())
    # N개만큼 배열에 입력받기
    arr_v = list(map(int, input().split()))
    # 초기값 설정
    max_v = 0
    min_v = 1000000 # 문제의 조건에서 가능한 최대합
 
    # (N-M)을 앞뒤로 구해서 합해주면 됨
    for i in range(0, N-M+1): # 0,1,2
        sum = 0
        for j in range(i, i+M): # 0,1
            sum += arr_v[j]
        if max_v < sum:
            max_v = sum
        if min_v > sum:
            min_v = sum
    print(f'#{tc} {max_v - min_v}')