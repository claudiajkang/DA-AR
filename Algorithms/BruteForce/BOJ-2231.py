from sys import stdin

n = int(stdin.readline().rstrip())
res = 0

for i in range(1, 10 ** 6 + 1):
    s = i
    for j in str(i):
        s += int(j)

    if s == n:
        res = i
        break

print(res)
