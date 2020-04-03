from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

t = 0
res = ""
while True:
    n, m = map(int, read().split())

    if n == 0 and m == 0:
        print(res[:-1])
        break

    t += 1
    adj = [[] for i in range(n + 1)]

    for i in range(m):
        u, v = map(int, read().split())
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    prev = [-1] * (n + 1)

    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            flag = True
            q = deque()
            visited[i] = True
            q.append(i)

            while q:
                curr = q.popleft()

                for nxt in adj[curr]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        prev[nxt] = curr
                        q.append(nxt)

                    elif nxt != prev[curr]:
                        flag = False

            if flag:
                result += 1

    if result == 0:
        res += f"Case {t}: No trees.\n"
    elif result == 1:
        res += f"Case {t}: There is one tree.\n"
    else:
        res += f"Case {t}: A forest of {result} trees.\n"
