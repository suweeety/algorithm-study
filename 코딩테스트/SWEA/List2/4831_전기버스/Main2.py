for t in range(1, int(input())+1):
    k, n, m = map(int, input().split())
    station = [False] * n
    for s in list(map(int, input().split())):
        station[s] = True
     
    def ride(bus, cnt):
        nxt = bus + k
        if nxt >= n:
            return cnt
         
        for x in range(nxt, bus, -1):
            if station[x]:
                return ride(x, cnt+1)
        return 0
 
    print(f'#{t} {ride(0, 0)}')

