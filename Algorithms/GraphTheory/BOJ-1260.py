from sys import stdin
import queue


N, M, V = map(int, stdin.readline().split())
G = {}

for i in range(M):
    A, B = map(int, stdin.readline().split())

    if A not in G.keys():
        G[A] = []

    if B not in G.keys():
        G[B] = []

    G[A].append(B)
    G[B].append(A)

if V not in G.keys():
    print('{}\n{}'.format(str(V), str(V)))

else:
    for i in G.keys():
        G[i] = sorted(G[i])

    dstack = [V]
    dvisit = []

    while dstack:
        cur = dstack.pop()

        for i in reversed(G[cur]):
            if str(i) not in dvisit:
                dstack.append(i)

        if str(cur) not in dvisit:
            dvisit.append(str(cur))

    vqueue = queue.Queue()
    vqueue.put(V)
    vvisit = []

    while len(vqueue.queue):
        cur = int(vqueue.get())

        for i in G[cur]:
            if str(i) not in vvisit:
                vqueue.put(str(i))

        if str(cur) not in vvisit:
            vvisit.append(str(cur))

    if len(dvisit) != N or len(vvisit) != N:
        for i in sorted(G.keys()):
            if str(i) not in dvisit:
                dvisit.append(str(i))
            if str(i) not in vvisit:
                vvisit.append(str(i))

    print(' '.join(dvisit))
    print(' '.join(vvisit))
