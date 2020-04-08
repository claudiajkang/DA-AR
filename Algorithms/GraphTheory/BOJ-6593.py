from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

result = ""
p = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
while True:
    l, r, c = map(int, read().split())

    if [l, r, c] == [0, 0, 0]:
        print(result[:-1], end="")
        break

    g = [[['#'] * (c + 2) for i in range(r + 2)] for k in range(l + 1)]
    cur = [0, 0, 0]
    end = [0, 0, 0]

    for ll in range(1, l + 1):
        for rr in range(1, r + 1):
            g[ll][rr] = ['#'] + list(read()) + ['#']
            if g[ll][rr].count('S'):
                cur = [ll, rr, g[ll][rr].index('S')]

            if g[ll][rr].count('E'):
                end = [ll, rr, g[ll][rr].index('E')]

        temp = read()

    q = deque()
    q.append(cur + [0])
    done = False
    res = 0

    while q and not done:
        ch, ci, cj, ct = q.popleft()

        for hh, ii, jj in p:
            th, ti, tj = hh + ch, ii + ci, jj + cj

            if (1 <= th <= l) and (1 <= ti <= r) and (1 <= tj <= c):
                if [th, ti, tj] == end:
                    res = ct + 1
                    done = True
                    break
                if g[th][ti][tj] == '.':
                    g[th][ti][tj] = ct + 1
                    q.append([th, ti, tj, ct + 1])

    result += f"Escaped in {res} minute(s)." if res > 0 else "Trapped!"
    result += "\n"
