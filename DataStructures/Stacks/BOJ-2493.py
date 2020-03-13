from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
h = [0] + list(map(int, read().split()))
stack = []
r = [0] * (n+1)

for i in range(1, n+1):
    while stack:
        if stack and stack[-1][1] >= h[i]:
            break

        if stack and stack[-1][1] < h[i]:
            stack.pop()

    if stack:
        r[i] = stack[-1][0]

    stack.append([i, h[i]])

for i in range(1, n+1):
    print(r[i], end = ' ')