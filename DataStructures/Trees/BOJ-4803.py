from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

case = 1
while True:
    n, m = map(int, read().split())

    if n == 0 and m == 0:
        break

    tree = [[] for i in range(n + 1)]

    for i in range(m):
        a, b = map(int, read().split())
        tree[a].append(b)
        tree[b].append(a)

    prev = [-1] * (n + 1)
    visited = [False] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = True
            flag = True

            while q:
                cur = q.popleft()

                for j in tree[cur]:
                    if not visited[j]:
                        prev[j] = cur
                        visited[j] = True
                        q.append(j)

                    elif prev[cur] != j:
                        flag = False

                if not flag:
                    break

            if flag:
                result += 1

    if result == 0:
        print(f"Case {case}: No trees.")

    elif result == 1:
        print(f"Case {case}: There is one tree.")

    else:
        print(f"Case {case}: A forest of {result} trees.")

    case += 1
