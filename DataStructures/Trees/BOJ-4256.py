from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def poso(po, io):
    global res
    if len(po) == 0 or len(io) == 0:
        return

    idx = io.index(po[0])
    poso(po[1:idx + 1], io[:idx])
    poso(po[idx + 1:], io[idx + 1:])
    res.append(po[0])


t = int(read())
result = ""
for tt in range(t):
    n = int(read())
    preo = list(map(int, read().split()))
    ino = list(map(int, read().split()))
    res = []
    poso(preo, ino)
    result += ' '.join(map(str, res)) + '\n'

print(result[:-1], end="")
