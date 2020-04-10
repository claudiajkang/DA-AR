from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

case = 1
result = ""
while True:
    n, m = map(int, read().split())

    if n == 0 and m == 0:
        print(result[:-1], end="")
        break

    g = [[] for i in range(n + 1)]

    for i in range(m):
        a, b = map(int, read().split())
        g[a].append(b)
        g[b].append(a)

    visited = [False] * (n + 1)
    prev = [-1] * (n + 1)
    tree = 0

    for i in range(1, n + 1):
        if not visited[i]:
            q = deque()
            visited[i] = True
            q.append(i)
            flag = True

            while q:
                cur = q.popleft()

                for j in g[cur]:
                    if not visited[j]:
                        prev[j] = cur
                        visited[j] = True
                        q.append(j)

                    elif j != prev[cur]:
                        flag = False
                        break

            if flag:
                tree += 1

    if tree == 0:
        result += f"Case {case}: No trees.\n"

    elif tree == 1:
        result += f"Case {case}: There is one tree.\n"

    else:
        result += f"Case {case}: A forest of {tree} trees.\n"

    case += 1
