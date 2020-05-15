from sys import stdin
read = lambda: int(stdin.readline().rstrip())

n = read()
p = [0] * 10001

for i in range(n):
    l = read()
    p[l] += 1

for i in range(1, 10001):
    for j in range(p[i]):
        print(i)
