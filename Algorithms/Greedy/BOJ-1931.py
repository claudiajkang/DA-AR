from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
time = [[] for i in range(n)]

for i in range(n):
    time[i] = list(map(int, read().split()))

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])

temp = time[0][1]
res = 1

for i in range(1, n):
    if temp <= time[i][0]:
        res += 1
        temp = time[i][1]

print(res)
