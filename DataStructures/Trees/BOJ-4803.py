from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())


class Node:
    def __init__(self):
        self.data = 0
        self.con = []


case = 1
while True:
    n, m = read()
    if [n, m] == [0, 0]:
        break

    tree = [Node() for i in range(n + 1)]

    for i in range(m):
        a, b = read()
        tree[a].con.append(b)
        tree[b].con.append(a)

    visited = [False] * (n + 1)
    prev = [-1] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            q = deque()
            q.append(i)
            flag = True

            while q:
                cur = q.popleft()

                for j in tree[cur].con:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
                        prev[j] = cur

                    elif j != prev[cur]:
                        flag = False
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
