from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
hw = [list(map(int, read().split())) for i in range(n)]

hw.sort(key=lambda x: x[0])
hw.sort(reverse=True, key=lambda x: x[1])

day = [0] * 1001

for d, s in hw:
    for j in range(d, 0, -1):
        if day[j] == 0:
            day[j] = s
            break

print(sum(day))
