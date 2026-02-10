for tc in range(1, 11):
    n = int(input())
    line = [input() for i in range(8)]
    temp = []
    temp2 = []
    cnt = 0
    start = 0
    for i in range(0, 8):
        for j in range(0, 8-n+1):
            temp.clear()
            temp2.clear()
            for k in range(n):
                temp.append(line[i][j+k])
                temp2.append(line[j+k][i])
            if temp == temp[::-1]:
                cnt += 1
            if temp2 == temp2[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')