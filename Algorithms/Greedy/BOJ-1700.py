from sys import stdin

read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
e = list(map(int, read().split()))
elec = {i: [] for i in set(e)}

for i in range(k):
    elec[e[i]].append(i)

q = []
res = 0
for i in range(k):
    o = e[i]

    if o in q:
        elec[o].pop(0)
        continue

    if len(q) == n:
        tq = []

        for i in q:
            if len(elec[i]) == 0:
                tq.append([k + 1, i])
                break
            tq.append([elec[i][0], i])

        tq.sort(key=lambda x: x[0], reverse=True)
        q.remove(tq[0][1])
        res += 1

    q.append(o)
    elec[o].pop(0)

print(res)
