from sys import stdin
read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
a = [int(read()) for _ in range(n)]
a.sort(reverse=True)

c = 0
r = k

for i in a:
    if i <= r:
        c += (r // i)
        r -= i * (r // i)

    if r == 0:
        break

print(c)
