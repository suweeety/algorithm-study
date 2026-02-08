from itertools import combinations
for tc in range(1, int(input())+1):
    a = [i for i in range(1, 13)]
    n, k = map(int, input().split())
    
    answer = 0
    # combinations(리스트, 개수)는 모든 조합을 튜플 형태로 반환
    for i in combinations(a, n):
        if sum(i) == k:
            answer += 1

    print(f"#{tc} {answer}")