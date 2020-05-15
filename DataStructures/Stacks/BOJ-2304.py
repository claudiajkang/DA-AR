from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
h = [0] * 1001
endindex = 0

for i in range(n):
    l, lh = map(int, read().split())
    h[l] = lh
    endindex = max(endindex, l)

highest = h.index(max(h))
stack = [0]
res = 0

for i in range(highest+1):
    if h[stack[-1]] < h[i]:
        lh = stack.pop()
        res += (i-lh) * h[lh]
        stack.append(i)

stack = [0]

for i in range(endindex, highest-1, -1):
    if h[stack[-1]] <= h[i]:
        lh = stack.pop()
        res += abs(lh-i) * h[lh]
        stack.append(i)

while stack:
    res += h[stack.pop()]

print(res)
