n = int(input())

for i in range(n):
    R, P = input().split()
    R = int(R)
    result = [ch * R for ch in P]
    print(*result, sep = "")