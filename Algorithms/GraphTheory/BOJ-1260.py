from sys import stdin
import queue

N, M, V = map(int, stdin.readline().strip().split())
g = {}

for i in range(M):
    t = list(map(int, stdin.readline().strip().split()))

    if t[0] not in g.keys():
        g[t[0]] = []

    if t[-1] not in g.keys():
        g[t[-1]] = []

    g[t[0]].append(t[-1])
    g[t[-1]].append(t[0])

if V not in g.keys():
    print(V)
    print(V)

else:
    for i in g.keys():
        g[i] = sorted(g[i])

    dstack = [V]
    dvisit = []

    while dstack:
        cur = dstack.pop()
        if str(cur) not in dvisit:
            dvisit.append(str(cur))
        else:
            continue
        for i in reversed(g[cur]):
            if str(i) not in dvisit:
                dstack.append(i)

    vqueue = queue.Queue()
    vqueue.put(V)
    vvisit = []

    while vqueue.queue:
        cur = vqueue.get()
        if str(cur) not in vvisit:
            vvisit.append(str(cur))
        else:
            continue
        for i in g[cur]:
            if str(i) not in vvisit:
                vqueue.put(i)


    if len(dvisit) != N and len(vvisit) != N:
        for i in g.keys():
            if str(i) not in dvisit:
                dvisit.append(str(i))
            if str(i) not in vvisit:
                vvisit.append(str(i))

    print(' '.join(dvisit))
    print(' '.join(vvisit))