from sys import stdin

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

    dstack = [V]
    dvisit = []
    gn = len(g.keys())


    for i in g.keys():
        g[i] = sorted(g[i])

    while True:
        if dstack:
            cur = dstack.pop()
            for i in reversed(g[cur]):
                if (str(i) not in dvisit) and (i in dstack):
                    idx = dstack.index(i)
                    v = dstack.pop(idx)
                    dstack.append(v)
                elif str(i) not in dvisit:
                    dstack.append(i)

            if str(cur) not in dvisit:
                dvisit.append(str(cur))
        else:
            break

    if len(dvisit) != N:
        for i in g.keys():
            if str(i) not in dvisit:
                dvisit.append(str(i))

    bqueue = [V]
    bvisit = []

    while True:
        if bqueue:
            cur = bqueue.pop(0)
            for i in g[cur]:
                if str(i) not in bvisit:
                    bqueue.append(i)

            if str(cur) not in bvisit:
                bvisit.append(str(cur))
        else:
            break

    if len(bvisit) != N:
        for i in g.keys():
            if str(i) not in bvisit:
                bvisit.append(str(i))

    print(' '.join(dvisit))
    print(' '.join(bvisit))