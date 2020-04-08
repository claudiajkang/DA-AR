from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

results = ""
case = 1
while True:
    n, m = map(int, read().split())

    if [n, m] == [0, 0]:
        print(results[:-1])
        break

    tree = [[] for i in range(n + 1)]

    for i in range(m):
        a, b = map(int, read().split())
        tree[a].append(b)
        tree[b].append(a)

    prev = [-1] * (n + 1)
    visited = [False] * (n + 1)

    count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            q = deque()
            visited[i] = True
            q.append(i)
            flag = True

            while q:
                cur = q.popleft()

                for j in tree[cur]:
                    if not visited[j]:
                        visited[j] = True
                        prev[j] = cur
                        q.append(j)

                    elif j != prev[cur]:
                        flag = False
                        break

            if flag:
                count += 1

    results += f"Case {case}: "
    if count == 0:
        results += "No trees.\n"

    elif count == 1:
        results += "There is one tree.\n"

    else:
        results += f"A forest of {count} trees.\n"

    case += 1
