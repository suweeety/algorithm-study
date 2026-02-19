# 1. N(학생 수), M(벌점 횟수), K(기준 벌점) 입력
N, M, K = map(int, input().split())

# 2. 각 학생의 벌점 횟수를 저장할 리스트 (학생 번호가 1번부터이므로 N+1 크기)
cnt = [0] * (N + 1)
result = -1

# 3. M번의 벌점 기록을 하나씩 확인
for _ in range(M):
    student = int(input())

    if result == -1:
        cnt[student] += 1

        if cnt[student] == K:
            result = student

print(result)