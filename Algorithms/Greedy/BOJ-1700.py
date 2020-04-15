from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, k = read()
ed = list(read())
ec = {i: [] for i in set(ed)}

for i in range(k):
    ec[ed[i]].append(i)

q = []
res = 0

for i in range(k):
    o = ed[i]

    if o in q:
        if ec[o]: ec[o].pop(0)
        continue

    if len(q) >= n:
        temp = []
        for j in q:
            if len(ec[j]) == 0:
                temp.append([101, j])
                break
            else:
                temp.append([ec[j][0], j])

        temp.sort(reverse=True, key=lambda x: x[0])
        q.pop(q.index(temp[0][1]))
        res += 1

    q.append(o)
    if ec[o]:
        ec[o].pop(0)

print(res)
