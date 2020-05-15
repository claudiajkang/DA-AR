from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(1, 10 ** 6 + 1):
    s = i
    for j in str(i):
        s += int(j)

    if s == n:
        print(i)
        exit()

print(0)
