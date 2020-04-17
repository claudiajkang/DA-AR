from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
k = int(read())
sensor = list(map(int, read().split()))
sensor.sort()

if k >= n:
    print(0)
    exit()

dist = [0] * (n - 1)

for i in range(n - 1):
    dist[i] = sensor[i + 1] - sensor[i]

dist.sort(reverse=True)

for i in range(k - 1):
    dist[i] = 0

print(sum(dist))
