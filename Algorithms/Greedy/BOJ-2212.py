from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
k = int(read())
pos = list(map(int, read().split()))
pos.sort()

diff = [0] * (n - 1)

for i in range(n - 1):
    diff[i] = (pos[i + 1] - pos[i])

diff.sort(reverse=True)

print(sum(diff[k - 1:]))
