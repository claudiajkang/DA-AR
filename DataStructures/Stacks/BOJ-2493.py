from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
t = list(map(int, read().split()))
res = [0] * n
stack = [0]

for i in range(1, n):
    while stack and t[stack[-1]] < t[i]:
        stack.pop()

    if stack:
        res[i] = stack[-1] + 1
    stack.append(i)

for i in res:
    print(i, end = ' ')
