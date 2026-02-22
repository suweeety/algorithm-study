# 중위 순회 함수
def in_order(n):
    global ans
    if n <= N:
        in_order(n*2)
        ans += tree[n]
        in_order(n*2+1)

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1) # 1번 인덱스부터 사용
    ans = ''

    for _ in range(N):
        arr = input().split()
        idx = int(arr[0])
        char = arr[1]
        tree[idx] = char # 노드 번호에 해당하는 위치에 문자 저장

    in_order(1) # 루트 1번부터 순회
    print(f'#{tc} {ans}')