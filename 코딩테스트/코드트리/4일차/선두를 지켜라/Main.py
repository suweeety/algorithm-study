n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
# 1. A와 B의 매 초 시점의 위치(누적 거리)를 저장할 리스트
pos_a = [0]
pos_b = [0]

# 2. 이미 입력받은 v, t 리스트를 이용해 A의 위치 계산
curr_a = 0
for i in range(n):
    for _ in range(t[i]):
        curr_a += v[i]
        pos_a.append(curr_a)

# 3. 이미 입력받은 v2, t2 리스트를 이용해 B의 위치 계산
curr_b = 0
for i in range(m):
    for _ in range(t2[i]):
        curr_b += v2[i]
        pos_b.append(curr_b)

# 4. 선두가 바뀌는 횟수 계산
leader = 0 # 0: 동점, 1: A가 선두, 2: B가 선두
changes = 0

# 전체 시간 동안 매 초 비교 (A와 B의 총 이동 시간은 동일함)
for i in range(1, len(pos_a)):
    if pos_a[i] > pos_b[i]:
        if leader == 2: # 직전 선두가 B였다가 A로 바뀐 경우
            changes += 1
        leader = 1
    elif pos_b[i] > pos_a[i]:
        if leader == 1: # 직전 선두가 A였다가 B로 바뀐 경우
            changes += 1
        leader = 2
    # 두 위치가 같으면(동점) leader를 바꾸지 않음 (문제 조건 준수)

print(changes)