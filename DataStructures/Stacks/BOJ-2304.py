from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
h = [0] * 1001
ei = 0
highest = 0

for i in range(n):
    x, l = map(int, read().split())
    h[x] = l
    highest = max(highest, h[x])
    ei = max(ei, x)

hi = h.index(highest)
stack = [0]
res = 0

for i in range(hi+1):
    if stack and h[stack[-1]] <= h[i]:
        x = stack.pop()
        res += (i-x) * h[x]
        stack.append(i)

stack = [0]

for i in range(ei, hi-1, -1):
    if stack and h[stack[-1]] <= h[i]:
        x = stack.pop()
        res += abs(x-i) * h[x]
        stack.append(i)

while stack:
    res += h[stack.pop()]

print(res)