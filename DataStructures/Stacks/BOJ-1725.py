from sys import stdin
read = lambda: int(stdin.readline().rstrip())

n = int(read())
h = [read() for i in range(n)] + [0]
stack = []
res = 0

for i in range(n+1):
    while stack and h[stack[-1]] > h[i]:
        th = stack.pop()
        wd = i - stack[-1] - 1 if stack else i
        res = max(res, h[th]*wd)
    stack.append(i)

print(res)