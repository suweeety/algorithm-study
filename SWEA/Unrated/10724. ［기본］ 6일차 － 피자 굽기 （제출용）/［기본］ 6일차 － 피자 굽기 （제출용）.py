from collections import deque

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))

    pizza = deque([idx+1, val] for idx, val in enumerate(cheese))
    last_pizza = 0
    fire = deque()
    for _ in range(n):
        fire.append(pizza.popleft())

    while fire:
        idx, chez = fire.popleft()
        chez //= 2
        if chez > 0:
            fire.append([idx, chez])
        else:
            if pizza:
                fire.append(pizza.popleft())
            else:
                last_pizza = idx
    
    print(f'#{tc} {last_pizza}')