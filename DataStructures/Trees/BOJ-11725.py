import sys

sys.setrecursionlimit(10 ** 6)


def solve(n):
    global parent
    for i in l[n]:
        if parent[i] == 0:
            parent[i] = n
            solve(i)


n = int(input())
l = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

parent = [0 for _ in range(n + 1)]
parent[1] = 1

solve(1)

for i in range(2, n + 1):
    print(parent[i])
