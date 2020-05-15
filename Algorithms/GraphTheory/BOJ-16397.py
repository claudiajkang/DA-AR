from collections import deque
from sys import stdin

n, t, g = map(int, stdin.readline().rstrip().split())

if n == g:
    print(0)

else:
    b = [-1] * 10 ** 6

    q = deque()
    q.append(n)
    b[n] = 0
    suc = False

    while q:
        cur = q.popleft()

        if b[cur] > t:
            break

        if cur == g:
            suc = True
            break

        temp = [cur + 1, cur * 2]

        for i in range(2):
            if temp[i] > 99999:
                continue
            if i and temp[i]:
                temp[i] -= 10 ** (len(str(temp[i])) - 1)
            if b[temp[i]] == -1:
                q.append(temp[i])
                b[temp[i]] = b[cur] + 1

    if suc:
        print(b[g])
    else:
        print("ANG")
