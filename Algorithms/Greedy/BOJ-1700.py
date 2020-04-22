from sys import stdin

read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
device = list(map(int, read().split()))
elec = {i: [] for i in set(device)}

for i in range(k):
    elec[device[i]].append(i)

q = []
res = 0

for i in range(k):
    e = device[i]

    if e in q:
        elec[e].pop(0)
        continue

    if len(q) == n:
        tq = []

        for tt in q:
            if len(elec[tt]) == 0:
                tq.append([k + 1, tt])
                break
            tq.append([elec[tt][0], tt])

        tq.sort(reverse=True, key=lambda x: x[0])
        q.remove(tq[0][1])
        res += 1

    q.append(e)
    elec[e].pop(0)

print(res)