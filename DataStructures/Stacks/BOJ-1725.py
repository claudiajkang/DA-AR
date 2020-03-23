from sys import stdin
read = lambda: int(stdin.readline().rstrip())

n = read()
stack = []
h = [read() for i in range(n)] + [0]
res = 0

for i in range(n+1):
    while stack and h[stack[-1]] > h[i]:
        t = stack.pop()
        wd = i - stack[-1] - 1 if stack else i
        res = max(res, wd * h[t])

    stack.append(i)

print(res)