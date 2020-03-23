from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
h = [0] * 1001
ei = 0

for i in range(n):
    idx, v = map(int, read().split())
    h[idx] = v
    ei = max(ei, idx)

highest = max(h)
hi = h.index(highest)

res = 0
stack = [0]
for i in range(hi+1):
    if stack and h[stack[-1]] <= h[i]:
        t = stack.pop()
        res += h[t] * (i - t)
        stack.append(i)

stack = [0]
for i in range(ei, hi-1, -1):
    if stack and h[stack[-1]] <= h[i]:
        t = stack.pop()
        res += h[t] * abs(i - t)
        stack.append(i)

while stack:
    res += h[stack.pop()]

print(res)
