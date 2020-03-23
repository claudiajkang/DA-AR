from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
h = [0] * 1001
end_idx = 0

for i in range(n):
    idx, v = map(int, read().split())
    h[idx] = v
    end_idx = max(end_idx, idx)

highest = max(h)
highest_idx = h.index(highest)
res = 0
stack = [0]
for i in range(highest_idx + 1):
    if stack and h[stack[-1]] <= h[i]:
        idx = stack.pop()
        res += (i - idx) * h[idx]
        stack.append(i)

stack = [0]
for i in range(end_idx, highest_idx - 1, -1):
    if stack and h[stack[-1]] <= h[i]:
        idx = stack.pop()
        res += (idx - i) * h[idx]
        stack.append(i)

while stack:
    res += h[stack.pop()]

print(res)