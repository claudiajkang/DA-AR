from sys import stdin
read = lambda: stdin.readline().rstrip()


def posto(po, io):
    global res

    if not po or not io: return

    idx = io.index(po[0])
    posto(po[1:idx + 1], io[:idx])
    posto(po[idx + 1:], io[idx + 1:])
    res.append(str(po[0]))


t = int(read())

for tt in range(t):
    n = int(read())

    preo = list(map(int, read().split()))
    ino = list(map(int, read().split()))
    res = []
    posto(preo, ino)

    print(' '.join(res))
