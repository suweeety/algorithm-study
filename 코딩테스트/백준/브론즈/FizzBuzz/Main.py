import sys
input = sys.stdin.readline

input_str = []
for _ in range(3):
    input_str.append(input().strip())

# n = [0, 0, 0] 으로 미리 방을 만든다
n = [0] * 3
last_num = 0
last_idx = 0    

# 순회하면서 숫자를 찾기
for i in range(3):
    # input_str[i]가 숫자인지 확인하는 가장 쉬운 방법: .isdigit()
    if input_str[i].isdigit():
        n[i] = int(input_str[i])
        # 숫자를 찾았다면, 그 숫자가 몇 번째(i)에 있었는지 저장
        last_num = n[i]
        last_idx = i # 2

# 숫자 찾아서 몇번째인지 확인 후 4번째 값을 출력함
result = last_num + (3-last_idx)

# 출력 시 조건은 위 주석 참고
if result % 3 == 0 and result % 5 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)