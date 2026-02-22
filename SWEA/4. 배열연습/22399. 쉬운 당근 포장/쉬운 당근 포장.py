for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    min_v = N       

    for i in range(N-2):
        for j in range(i+1, N-1):
            # 칼질한 바로 앞 당근과 뒤 당근의 크기가 같으면 패스
            if arr[i] == arr[i+1] or arr[j] == arr[j+1]:
                continue

            s = i+1
            m = j-i
            l = N-1-j

            if min_v > max(s, m, l) - min(s, m, l):
                min_v = max(s, m, l) - min(s, m, l)
    if min_v == N:
        min_v = -1
    print(f'#{tc} {min_v}')