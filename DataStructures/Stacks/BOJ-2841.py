from sys import stdin
read = lambda: map(int, stdin.readline().rstrip().split())

n, p = read()
stack = [[] for i in range(n)]
res = 0

for i in range(n):
    ln, lp = read()

    while stack[ln] and stack[ln][-1] > lp:
        stack[ln].pop()
        res += 1

    if not lp in stack[ln]:
        stack[ln].append(lp)
        res += 1

print(res)