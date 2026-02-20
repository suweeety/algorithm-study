def in_order(v):
    if v >= len(tree) or tree[v] is None:
        return
    in_order(v*2)
    ans.append(tree[v])
    in_order(v*2+1)

for tc in range(1, int(input())+1):
    N = int(input())
    tree = [None]
    ans = [None]
    for i in range(1, N+1):
        tree.append(i)
    in_order(1)

    ans_1 = tree[ans.index(1)]
    ans_2 = tree[ans.index(N//2)]
    print(f'#{tc} {ans_1} {ans_2}')