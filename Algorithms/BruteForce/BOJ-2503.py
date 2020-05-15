from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
t = ['0'] * n
sb = [[] for i in range(n)]

for i in range(n):
    a, b, c = map(int, read().split())
    t[i] = str(a)
    sb[i] = [b, c]

res = 0

for i in range(101, 999):
    temp = str(i)
    if len(set(temp)) != 3: continue
    if '0' in temp: continue

    count = 0

    for tt in range(n):
        test = t[tt]
        tc = [0, 0]

        for j in range(3):
            if temp[j] == test[j]:
                tc[0] += 1
                continue

            if temp[j] in test:
                tc[1] += 1

        if tc == sb[tt]:
            count += 1

    if count == n:
        res += 1

print(res)