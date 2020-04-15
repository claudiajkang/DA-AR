from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, k = read()
order = list(read())
elec = {i: [] for i in set(order)}

for i in range(k):
    o = order[i]
    elec[o].append(i)

res = 0
q = []

for i in range(k):
    o = order[i]
    if o in q:
        if elec[o]: elec[o].pop(0)
        continue

    if len(q) < n:
        if elec[o]: elec[o].pop(0)
        q.append(o)
        continue

    temp = []
    isZero = False
    zi = 0

    for t in q:
        if len(elec[t]) == 0:
            isZero = True
            zi = t
            break

        temp.append([elec[t], t])

    if isZero:
        q.pop(q.index(zi))
    else:
        temp.sort(reverse=True, key=lambda x: x[0])
        t = q.pop(q.index(temp[0][1]))

    if elec[o]:
        elec[o].pop(0)
    q.append(o)
    res += 1

print(res)
