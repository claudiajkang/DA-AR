from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

cs = 1
res = ""
while True:
    n, m = map(int, read().split())

    if n == 0 and m == 0:
        print(res[:-1])
        break

    tree = [[] for i in range(n + 1)]

    for i in range(m):
        a, b = map(int, read().split())
        tree[a].append(b)
        tree[b].append(a)

    prev = [-1] * (n + 1)
    visited = [False] * (n + 1)
    results = 0

    for i in range(1, n + 1):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = True
            flag = True

            while q:
                cur = q.popleft()
                for nxt in tree[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        prev[nxt] = cur
                        q.append(nxt)
                        continue

                    if nxt != prev[cur]:
                        flag = False

            if flag:
                results += 1

    res += f"Case {cs}: "

    if results == 0:
        res += "No trees.\n"

    elif results == 1:
        res += "There is one tree.\n"

    else:
        res += f"A forest of {results} trees.\n"

    cs += 1
