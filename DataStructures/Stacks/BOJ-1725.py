from sys import stdin
read = lambda: int(stdin.readline().rstrip())

n = read()
h = [0] * (n+1)
stack = []
res = 0

for i in range(n+1):
    if i < n:
        h[i] = read()

    while stack and h[stack[-1]] > h[i]:
        x = stack.pop()
        wd = i - stack[-1] - 1 if stack else i
        res = max(res, wd * h[x])

    stack.append(i)

print(res)
