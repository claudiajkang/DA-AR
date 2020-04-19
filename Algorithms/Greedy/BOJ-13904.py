from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
hw = []
day = 0

for i in range(n):
    d, w = map(int, read().split())

    day = max(d, day)
    hw.append([d, w])

hw.sort(key=lambda x: x[1], reverse=True)

res = [0] * (day + 1)

for d, w in hw:
    if res[d] == 0:
        res[d] = w
    else:
        for j in range(d - 1, 0, -1):
            if res[j] == 0:
                res[j] = w
                break

print(sum(res))
