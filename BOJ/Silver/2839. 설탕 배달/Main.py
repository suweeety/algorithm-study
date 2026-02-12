N = int(input())
sum_v = 0
result = False

while N >= 0:
    if N % 5 == 0:
        sum_v += (N // 5)
        result = True
        break
    else: 
        N -= 3
        sum_v += 1

if result:
    print(sum_v)
else:
    print(-1)