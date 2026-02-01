import sys

input = sys.stdin.readline

# 숫자의 범위만큼(1~10000) 바구니를 만든다
# 8MB 제한이므로 10,001개의 0이 들어있는 리스트는 충분히 들어간다
check_list = [0] * 10001

n = int(input())

# 2. 숫자를 입력받자마자 해당 바구니의 카운트를 1올린다
# 숫자를 리스트에 저장하지 않고 개수만 세고 바로 버리는게 핵심
for _ in range(n):
    num = int(input())
    check_list[num] += 1

for i in range(10001):
    if check_list[i] != 0:
        for _ in range(check_list[i]):
            print(i)