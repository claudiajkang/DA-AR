from sys import stdin
read = lambda: map(int, stdin.readline().rstrip().split())

n, p = read()
stack = [[] for i in range(n+1)]
res = 0

for i in range(n):
    m, mp = read()

    while stack[m] and stack[m][-1] > mp:
        stack[m].pop()
        res += 1

    if mp not in stack[m]:
        res += 1
        stack[m].append(mp)

print(res)