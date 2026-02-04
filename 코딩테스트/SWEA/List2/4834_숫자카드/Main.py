T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input()))

    # 빈방 만들기
    temp = [0] * (10)
    
    # 개수 세기
    for i in arr:
        temp[i] += 1
    
    max_idx = 0
    # 최대값 구해서 출력
    for i in range(10):
        if temp[i] >= temp[max_idx]:
            max_idx = i
    
    print(f'#{tc+1} {max_idx} {temp[max_idx]}')