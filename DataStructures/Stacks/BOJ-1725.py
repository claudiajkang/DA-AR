from sys import stdin
read = lambda: int(stdin.readline().rstrip())

n = read()
h = [read() for _ in range(n)] + [0]

res = 0
stack = []
for i in range(n + 1):
    while stack and h[stack[-1]] >= h[i]:
        j = stack.pop()
        wd = i - stack[-1] - 1 if stack else i
        res = max(res, h[j] * wd)
    stack.append(i)

print(res)