from sys import stdin

read = lambda: stdin.readline().rstrip()

n, k = map(int, read().split())
t = list(map(int, read().split()))
elec = {i: [] for i in set(t)}

for i in range(k):
    elec[t[i]].append(i)

q = []
count = 0

for i in range(k):
    cur = t[i]

    if cur in q:
        elec[cur].pop(0)
        continue

    if len(q) == n:
        tl = []

        for i in q:
            if len(elec[i]) == 0:
                tl.append([k + 1, i])
                break
            else:
                tl.append([elec[i][0], i])

        tl.sort(key=lambda x: x[0], reverse=True)
        q.pop(q.index(tl[0][1]))
        count += 1

    q.append(cur)
    elec[cur].pop(0)

print(count)
