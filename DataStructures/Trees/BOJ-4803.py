from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

case = 1
while True:
    n, m = read()

    if [n, m] == [0, 0]: break

    g = [[] for i in range(n + 1)]

    for i in range(m):
        a, b = read()
        g[a].append(b)
        g[b].append(a)

    visited = [False] * (n + 1)
    res = 0
    prev = [-1] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            q = deque()
            q.append(i)
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

                if not flag: break

            if flag: res += 1

    if res == 0:
        print(f"Case {case}: No trees.")
    elif res == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {res} trees.")

    case += 1