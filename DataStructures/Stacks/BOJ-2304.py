from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
h = [0] * 1001
end = 0

for i in range(n):
    x, y = map(int, read().split())
    h[x] = y
    end = max(end, x)

highest = h.index(max(h))

stack = [0]
res = 0
for i in range(highest+1):
    if stack and h[stack[-1]] < h[i]:
        tx = stack.pop()
        res += (i - tx) * h[tx]
        stack.append(i)

stack = [0]
for i in range(end, highest-1, -1):
    if stack and h[stack[-1]] <= h[i]:
        tx = stack.pop()
        res += (tx - i) * h[tx]
        stack.append(i)

while stack:
    res += h[stack.pop()]

print(res)