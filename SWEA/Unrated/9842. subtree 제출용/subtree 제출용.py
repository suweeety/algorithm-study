def pre_order(v):   # v번 정점을 전위순위하는 코드
    global cnt
    if v:   # 0번 정점은 존재하지 않으므로
        cnt += 1    # visit(v)
        pre_order(left[v])
        pre_order(right[v])

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())    # 간선 수 E, 순회를 시작할 서브트리 N
    arr = list(map(int, input().split()))

    V = E + 1   # 정점 수 = 간선 수 + 1
    # 부모 번호를 인덱스로 자식 번호 저장
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:    # 왼쪽 자식이 아직 없으면
            left[p] = c     # c를 왼족자식으로 저장
        else:
            right[p] = c    # 오른쪽 자식이 있으면 왼쪽 자식으로 저장
    cnt = 0
    pre_order(N)    # 서브트리의 루트 N부터 순회하면서 서브트리의 정점 수 알아내기
    print(f'#{tc} {cnt}')