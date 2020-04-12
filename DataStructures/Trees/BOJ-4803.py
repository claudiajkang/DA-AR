from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

case = 1
while True:
    n, m = read()

    if n == 0 and m == 0: break

    g = [[] for i in range(n + 1)]

    for i in range(m):
        a, b = read()
        g[a].append(b)
        g[b].append(a)

    visited = [False] * (n + 1)
    prev = [-1] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = True
            flag = True

            while q:
                cur = q.popleft()

                for j in g[cur]:
                    if not visited[j]:
                        visited[j] = True
                        prev[j] = cur
                        q.append(j)

                    elif j != prev[cur]:
                        flag = False
                        break

                if not flag: break

            if flag:
                result += 1

    if result == 0:
        print(f"Case {case}: No trees.")
    elif result == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {result} trees.")

    case += 1