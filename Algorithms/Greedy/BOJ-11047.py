from sys import stdin

read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
coin = [[] for i in range(n)]
c = 0
sum = k

for i in range(n - 1, -1, -1):
    coin[i] = int(read())

for i in range(n):
    if coin[i] <= sum:
        q = sum // coin[i]
        sum -= (coin[i] * q)
        c += q

    if sum == 0:
        break

print(c)
