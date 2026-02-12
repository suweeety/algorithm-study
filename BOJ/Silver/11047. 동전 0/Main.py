n, k = map(int, input().split())

cash_arr = [int(input()) for _ in range(n)]
end = n
total = 0

for i in range(n):
    if k < cash_arr[i]:
       end = i
       break

while k > 0:
    for i in range(end-1, -1, -1):
        if k >= cash_arr[i]:
            total += k // cash_arr[i]
            k = k % cash_arr[i]
            break

print(total)