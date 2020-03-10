from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
m = int(read())
psum = [0] * (n+1)

for i in range(n):
    psum[i+1] = psum[i] + a[i]

for k in range(m):
    i, j = map(int, read().split())
    print(psum[j] - psum[i-1])
