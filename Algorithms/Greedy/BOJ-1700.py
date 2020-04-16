from sys import stdin

read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
order = list(map(int, read().split()))
elec = {i: [] for i in set(order)}

for i in range(k):
    elec[order[i]].append(i)

q = []

res = 0

for i in range(k):
    o = order[i]

    if o in q:
        if elec[o]: t = elec[o].pop(0)
        continue

    if len(q) == n:
        t = []

        for i in q:
            if len(elec[i]) == 0:
                t.append([101, i])
                break
            else:
                t.append([elec[i][0], i])

        t.sort(reverse=True, key=lambda x: x[0])
        idx = t[0][1]

        q.pop(q.index(idx))
        res += 1

    q.append(o)
    if elec[o]: elec[o].pop(0)

print(res)