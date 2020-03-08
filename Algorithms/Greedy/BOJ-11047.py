from sys import stdin
read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
a = [int(read()) for _ in range(n)]
a.sort(reverse=True)

r = k
c = 0

for i in a:
    if i <= r:
        c += (r // i)
        r = (r % i)
        if r == 0:
            break

print(c)
