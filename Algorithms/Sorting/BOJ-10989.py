from sys import stdin

read = lambda: int(stdin.readline().rstrip())

n = read()
PN = [0] * 10001

for i in range(n):
    l = read()
    PN[l] += 1

for i in range(1, 10001):
    for j in range(PN[i]):
        print(i)
