from sys import stdin
read = lambda: int(stdin.readline().rstrip())

n = read()
h = [read() for i in range(n)] + [0]
stack = [0]
res = 0

for i in range(1, n+1):
    while stack and h[stack[-1]] > h[i]:
        c = stack.pop()
        wd = i - stack[-1] - 1 if stack else i
        res = max(res, h[c] * wd)

    stack.append(i)

print(res)
