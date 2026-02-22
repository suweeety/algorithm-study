T = int(input())
for tc in range(1, T+1):
    pass
    # k 찾기,
    P, Pa, Pb = map(int, input().split())
 
    def binary_search(P, Pa):
        pass
        l = 1 #시작
        r = P #종료
        cnt = 0
        while l <= r:
            # 중간값
            c = (l + r)//2 #200
            if c == Pa:
                return cnt
            elif c > Pa: # 왼쪽 탐색
                r = c
            else: # 오른쪽 탐색
                l = c
            cnt += 1
        return -1
 
    a = binary_search(P, Pa)
    b = binary_search(P, Pb)
    winner = 0
    if a < b:
        winner = 'A'
    elif a > b:
        winner = 'B'
    print(f'#{tc} {winner}')