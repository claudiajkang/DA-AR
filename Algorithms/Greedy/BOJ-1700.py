from sys import stdin

read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
temp = list(map(int, read().split()))
elec = {i: [] for i in set(temp)}

for i in range(k):
    o = temp[i]
    elec[o].append(i)

q = []
count = 0
for i in range(k):
    o = temp[i]

    if o in q:
        elec[o].pop(0)
        continue

    if len(q) == n:
        tq = []

        for t in q:
            if len(elec[t]) == 0:
                tq.append([k + 1, t])
                break
            else:
                tq.append([elec[t][0], t])

        tq.sort(reverse=True, key=lambda x: x[0])

        q.remove(tq[0][1])
        count += 1

    q.append(o)
    elec[o].pop(0)

print(count)
