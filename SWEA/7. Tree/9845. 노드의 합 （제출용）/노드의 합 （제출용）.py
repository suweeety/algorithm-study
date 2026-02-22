def post_order(v):
    if v > N:   # 존재하지 않는 자식노드면(왼쪽자식만 있는 경우)
        return 0
    elif tree[v]: # 값이 있으면 리프노드
        return tree[v]
    else:       # 리프노드가 아니면 왼쪽 자식과 오른쪽 자식의 합 계산
        left = post_order(v*2) # 완전이진트리 왼쪽 자식
        right = post_order(v*2+1) # 완전이진트리 오른쪽 자식
        tree[v] = left + right
        return tree[v]
 
T = int(input())
for tc in range(1, T+1):
    # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    # 완전이진트리를 저장하는 배열. 배열인덱스==노드번호
    tree = [0] * (N + 1)    # 1번부터 N번까지인 완전이진트리 노드
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value
 
    post_order(1)   # 루트부터 순회 시작
    print(f'#{tc} {tree[L]}')